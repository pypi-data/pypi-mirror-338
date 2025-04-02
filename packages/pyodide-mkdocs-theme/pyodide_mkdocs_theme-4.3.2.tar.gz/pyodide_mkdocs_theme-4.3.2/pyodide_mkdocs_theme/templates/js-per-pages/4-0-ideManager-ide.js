/*
pyodide-mkdocs-theme
Copyleft GNU GPLv3 🄯 2024 Frédéric Zinelli

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.
If not, see <https://www.gnu.org/licenses/>.
*/



import { escapePyodideCodeForJsTemplates } from 'functools'




/**Singleton object managing interactions between IDEs in the current page.
 *      - zip (import/export)
 *      - sequential run (in a version to come)
 * */
class GlobalIdesManagerBase {

  constructor(){
    this.allIdes = {}
  }

  registerIde(ide){
    this.allIdes[ide.id] = ide
  }
}






/** Common top level object.
 * */
class GlobalZipExportIdesManager extends GlobalIdesManagerBase {

  exportIdesAsZip(){

    const codesToArchive = this._getDataForExportableIdeInPage()
    const zipNameChunks = this._buildZipNameFirstChunks()
    const archiveFromPyCode = this._buildZipExportPythonCode(codesToArchive, zipNameChunks)

    pyodide.runPython(archiveFromPyCode)
  }



  /**Build an array of objects, containing all the needed info to load the archive content
   * back later (IDE's editorId, code and pyName).
   * */
  _getDataForExportableIdeInPage(){
    const toArchive = []
    for (const ide of Object.values(this.allIdes)){
      if(ide.export){
        const code = ide.getCodeToTest()
        const id   = ide.id
        const pyName = ide.pyName
        toArchive.push({code, id, pyName})
      }
    }
    return toArchive
  }



  _buildZipNameFirstChunks(){
    const zipChunks = []

    if(CONFIG.exportZipPrefix){
      zipChunks.push(CONFIG.exportZipPrefix)
    }
    if(CONFIG.exportZipWithNames){
      let names = ""
      while (!names){
        names = window.prompt(CONFIG.lang.zipAskForNames.msg)
      }
      zipChunks.push(names)
    }
    return zipChunks
  }


  /**Create the zip archive from within pyodide (because no need for new CDNs XD ),
   * then push it back to the JS layer.
   * */
  _buildZipExportPythonCode(codesToArchiveArr, zipNameChunks){

    const jsonArr        = JSON.stringify(codesToArchiveArr)
    const pyodideJsonArr = escapePyodideCodeForJsTemplates(jsonArr)

    return `
@__builtins__.auto_run
def _hack_build_zip():

    import shutil, json
    from pathlib import Path
    from itertools import count

    def unique_name(p:Path):
        while p.exists():
            p = p.with_name(f"{ p.stem }_{ p.suffix }")
        return p

    dirname = unique_name(Path('tmp_zip'))
    dirname.mkdir()

    url    = ${ JSON.stringify(location.href) }
    origin = ${ JSON.stringify(location.origin) }
    chunks = ${ JSON.stringify(zipNameChunks) }

    # Always make sure the url part of the filename is not empty:
    zip_url = url[len(origin):].strip('/').replace('/','_').replace('.','_') or 'home'
    chunks.append(zip_url)

    zip_name = unique_name( Path( '-'.join(chunks) + '.zip') )

    data = json.loads("""${ pyodideJsonArr }""")
    for ide in data:
        name = dirname / (ide['id'] + '${ CONFIG.ZIP.pySep }' + ide['pyName'])
        name.write_text(ide['code'], encoding="utf-8")

    shutil.make_archive(zip_name.with_suffix(''), 'zip', dirname)

    pyodide_downloader(
        zip_name.read_bytes(),
        zip_name.name,
        "application/zip",   # automatically "overridden in" "application/x-zip-compressed" on Windaube...
    )
    shutil.rmtree(dirname)
    zip_name.unlink()
`
  }
}








class GlobalZipImportIdesManager extends GlobalZipExportIdesManager{


  getArchiveFiles(dropEvent){
    const useItems = Boolean(dropEvent.dataTransfer.items)
    const zipFiles = [
      ...dropEvent.dataTransfer[ useItems?'items':'files' ]
    ].filter(this._isArchiveFile).map(
      itemOrFile => useItems ? itemOrFile.getAsFile() : itemOrFile
    )

    if(zipFiles.length != 1){
      console.log([...dropEvent.dataTransfer[ useItems?'items':'files' ]])
    }

    return zipFiles
  }


  _isArchiveFile=(itemOrFile)=>(
    itemOrFile.kind === "file" && [
      "application/zip", "application/x-zip-compressed"
    ].some(type=>type==itemOrFile.type)
  )


  readZipContentAndUpdateIdes(zipArchive){
    const reader = new FileReader();

    reader.onload = function(event){
      const bytesArr = event.target.result
      pyodide.unpackArchive(bytesArr, "zip", {extractDir: CONFIG.ZIP.tmpZipDir})
      pyodide.runPython(`
@__builtins__.auto_run
def _hack_zip_loading():
    from pathlib import Path
    import js

    tmp_dir = Path('${ CONFIG.ZIP.tmpZipDir }')

    for py in tmp_dir.iterdir():
        content = py.read_text(encoding='utf-8')
        js.config().loadIdeContent(py.name, content)
        py.unlink()

    tmp_dir.rmdir()
`)
    }

    reader.readAsArrayBuffer(zipArchive)
  }
}







/** Common top level object.
 * */
class GlobalIdesManager extends GlobalZipImportIdesManager {}



/**Public interface object */
export const IDES_MANAGER = (_ => {

  const IDE_MANAGER = new GlobalIdesManager()


  function getPublicMethodsWithInheritance(cls) {
    const methods = []
    while (cls.prototype) {
      const props = Object.getOwnPropertyNames(cls.prototype)
      for(const prop of props){
        if(!prop.startsWith('_') && prop!='constructor') {
          methods.push(prop)
        }
      }
      cls = Object.getPrototypeOf(cls)
    }
    return methods
  }

  /**Intermediate object to isolate the GlobalIdesManager from the visible elements
   * of the module.
   * Reason: currently, none of the IdeRunners objects are accessible to the user,
   * even by loading a module from the console. So trying to keep it that way with
   * this extra layer/wrapper.
    */
  const goodCommunicant = {}
  const methodsToPatch  = getPublicMethodsWithInheritance(GlobalIdesManager)
  for (const method of methodsToPatch){
    goodCommunicant[method] = ((method) => (...args) => IDE_MANAGER[method](...args))(method)
  }

  return goodCommunicant
})()