'''
## --------------------------------------------------------------------------
## SethPythonFunctions.py - Python Script
## --------------------------------------------------------------------------

  DESCRIPTION:
   A Class of Python Functions geared towards Asset Organization in Unreal Engine.
   This first one is: An Asset path updater
   
   The AssetPathUpdater method makes it easy to update multiple asset paths
   at the same time. 

   Instead of selecting individual assets > right clicking > re-importing with new file > 
   finding the files > confirming etc. Simply select as many as you want. Enter the old
   file path and then the new one and you're done. 
    
   Especially useful if you've changed names or locations of the folders where unreal expects
    to find them. 

  USAGE: 
    Step 1- Select an asset(s) from the content browser after running the Widget. 
    Step 2- Copy-paste the old file path into the text box: Old Path.
    Step 3- Copy-paste the new file path into the text box: New Path. 
   


## AUTHORS:
##  Seth Cipriano - sethcip@gmail.com


## VERSIONS:
    0.00 - Jan 17, 2022 - Beta Version.
    1.10 - Jan 18, 2022 - Fixed so also handles non-unique node names.
    1.20 - Feb 4, 2022 - Converts "\\" to "/" & UI is better
## --------------------------------------------------------------------------

'''

#Version 1.20
import unreal

@unreal.uclass()        
class SethPythonFunctions(unreal.BlueprintFunctionLibrary):   
    
    @unreal.ufunction(ret=str, params=[str,str] , static=True, meta=dict(Category="Seth Methods"))
     
    def AssetPathUpdater(search, replacement):
        
        search = search.replace("\\", "/")
        replacement = replacement.replace("\\", "/")
        
        AssetsToUpdate = unreal.EditorUtilityLibrary.get_selected_assets()
        
        for asset in AssetsToUpdate:    
            AssetName = asset.get_name()
                       
            AssetPathData = asset.get_editor_property("asset_import_data")
            AssetFileName = AssetPathData.extract_filenames()

            for assetIndex,assetFn in enumerate(AssetFileName):
                #assetFn = assetFn.replace("\\", "/")  ## Unnecessary b/c Unreal file paths have forward slashes already.
                NewPath = assetFn.replace(search, replacement)

                #confirmation it's working
                print(f"Search path is {search}")
                print(f"Replacement path is {replacement}")
                print(f"New path is {NewPath}")
                
            AssetPathData.scripted_add_filename(NewPath, assetIndex, "Source File")          
        msg = "Success!"
        return msg








'''
****Potential Bug Fixes****
- Whenever python file updates, need to recconnect a new node or right click and refresh





##  Minimal Notes  ##

        #print(f"Replacement path is {replacement}")
        #replacement = pathlib.PureWindowsPath(replacement).as_posix()
        #print(f"Replacement path is {replacement}")
        
        %% Ideas to increase functionality %% 

If you ever moved entire project you would want something like this to operate on entire project root.
Would want it to handle everything that has a source path in unreal.
Could list all importable things.

*have a check box to replace things only at start*

*have a button that populates the path of the selected assets with the existing path*

         %% Ideas to increase functionality %% 

'''