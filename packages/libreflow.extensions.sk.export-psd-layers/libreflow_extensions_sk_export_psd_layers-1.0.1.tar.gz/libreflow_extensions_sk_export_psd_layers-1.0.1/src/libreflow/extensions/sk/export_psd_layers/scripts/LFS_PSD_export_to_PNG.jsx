// Including JSON object for JSON file creation
#include "json.jsx";
// --------------------------------------
// Main function who export layers to PNG
// --------------------------------------
function _LFS_exportPSDLayersToPNG()
{
	var theDoc = app.activeDocument; // Get the active document name
	var folderName = theDoc.name.replace(/\..+$/, '')  // Remove the *.psd extension from the active document name
    
    $.writeln(folderName)
    
	var pathToTheFile = app.activeDocument.path+'/'+folderName;
    pathToTheFile = pathToTheFile.replace("_psb","_render")
     $.writeln(pathToTheFile)

//~ 
	var layersPrefix = folderName+"-"; // Add a dash after the name of the document
    
    var data = {
        from : theDoc.name,
        layers : [],
        hidden_layers : [],
        };
    
	var allLayersList = createLayersTree(theDoc, data); // Collect all layers name
	var layerCount = allLayersList.length; // Number of Layer in PSD file
	var windowsContent = ""; // Placeholder for the UI content
    
	windowsContent = "window{text:'Exporting each layer to PNG images',bounds:[100,100,800,160],"
	windowsContent += "bar:Progressbar{bounds:[20,10,680,50] , value:0,maxvalue:100}";
	windowsContent += "};" // Filling the UI;
	
	hideAllLayers(allLayersList);
	
	var win = new Window(windowsContent); // Creation of the main window with a simple progress bar

	win.center();
	win.show();
	
	for (var i = 0; i < layerCount; i++)
	{
		allLayersList[i].visible = 1; // Show one layer
		savePNGImage(layersPrefix+allLayersList[i].name,pathToTheFile); // Save it PNG
		win.bar.value = (i+1)*(100/layerCount); // Update the progress bar
		win.text = 'Exporting layer "'+allLayersList[i].name+'" to PNG image ('+(i+1)+'/'+layerCount+'). In progress ... please wait.'; // Update title of the window
		app.refresh(); // Force the refresh of photoshop interface
		allLayersList[i].visible = 0; // hide on layer
	}
    
    createJSONFile(data, pathToTheFile);

	showAllLayers();
	win.close();
    theDoc.save()
    executeAction(app.charIDToTypeID('quit'), undefined, DialogModes.NO);
}


// ---------------------------------
// Get render path
// ---------------------------------



// ---------------------------------
// List all 'ArtLayers' in the stack
// ---------------------------------
function createLayersTree(document, data)
{
	var list = []; //Create an array to store each object

	for (var i = 0; i < document.layers.length; i++)
	{
		if (document.layers[i].typename == 'ArtLayer' ||  'LayerSet')  //Filter to only list layers of "ArtLayer" or "LayerSet" type;
		{
			list.push (document.layers[i]); // Fill the list
             data["layers"].push(document.layers[i].name)
             if (document.layers[i].visible == false)
             {
                 data["hidden_layers"].push(document.layers[i].name)
             }
		}
//~         else if (obj[i].typename == 'LayerSet') 
//~         {
//~       $.writeln(list)
//~         loopLayers(obj[i].layers,list);
//~       $.writeln(list)
//~         } 
	}
	return list; // Return the array
}


// ---------------------------------------------------------------------------------
// Switch visibility of all layers to "On" using "actions" (to speed up the process)
// ---------------------------------------------------------------------------------
function showAllLayers()
{
		var doc = activeDocument;
	
		var ref = new ActionReference();
		ref.putEnumerated(cTID('Lyr '), cTID('Ordn'), cTID('Trgt'));
		var desc = new ActionDescriptor();
		desc.putReference(cTID('null'), ref);
		executeAction(sTID('selectAllLayers'), desc, DialogModes.NO);
	
		var ref = new ActionReference();
		ref.putEnumerated(cTID('Lyr '), cTID('Ordn'), cTID('Trgt'));
		var list = new ActionList();
		list.putReference(ref);
		var desc = new ActionDescriptor();
		desc.putList(cTID('null'), list);
		executeAction(cTID('Shw '), desc, DialogModes.NO);

		var background = doc.layers[doc.layers.length -1];
		if (background.isBackgroundLayer)
		{
			background.visible = true;
		}
}


// ---------------------------------------------------------------------------------
// Switch visibility of all layers to "Off" using "actions" (to speed up the process)
// ---------------------------------------------------------------------------------
function hideAllLayers(layers) {
//~ 	var doc = app.activeDocument;
//~ 	
//~ 	var ref = new ActionReference();
//~ 	ref.putEnumerated(cTID('Lyr '), cTID('Ordn'), cTID('Trgt'));
//~ 	var desc = new ActionDescriptor();
//~ 	desc.putReference(cTID('null'), ref);
//~ 	executeAction(sTID('selectAllLayers'), desc, DialogModes.NO);
//~ 	
//~ 	var ref = new ActionReference();
//~ 	ref.putEnumerated(cTID('Lyr '), cTID('Ordn'), cTID('Trgt'));
//~ 	var list = new ActionList();
//~ 	list.putReference(ref);
//~ 	var desc = new ActionDescriptor();
//~ 	desc.putList(cTID('null'), list);
//~ 	executeAction(cTID('Hd  '), desc, DialogModes.NO);


     var layerCount = layers.length;
     for (var i = 0; i < layerCount; i++)
	{
        layers[i].visible = 0;
     }
     

	var background = layers[layers.length -1];
	if (background.isBackgroundLayer) {
		background.visible = false;
	}
}

// ------------------------------------
// Save the document to a new PNG image
// ------------------------------------
function savePNGImage(nameOfFile,pathToTheFile)
{
	var folderToCreate = Folder(pathToTheFile); // Define the path to the new folder
	var theFullAbsolutePath = pathToTheFile+"/"+nameOfFile+".png"; // Define the full path to the new PNG file
	var opts; // Prepare export options

	if(!folderToCreate.exists)
	{
		folderToCreate.create(); // Create the folder if not existing
	}

	opts = new ExportOptionsSaveForWeb();
	opts.format = SaveDocumentType.PNG; // Define type "PNG"
	opts.PNG8 = false; // Because we want a "PNG24" (in fact "PNG32" because we want to keep the Alpha channel)
	opts.transparency = true; // True by default but ... just to be sure

	pngFile = new File(theFullAbsolutePath); // Define a new file object
	app.activeDocument.exportDocument(pngFile, ExportType.SAVEFORWEB, opts); // Now, it's time to export the PNG for good
}

//------------------------------------------------------
// Write layer order in .txt file
//-------------------------------------------------------

function createJSONFile(object, path){

  //define file 
  var jsonFile = new File(path+"/layers.json")
  //jsonFile.close();
  
//~   if(jsonFile.exists){
//~       jsonFile.remove()
//~       }
    //open file
    jsonFile.open("w")

    //write to file convert to string
    jsonFile.write(JSON.lave(object));

    //close file
    jsonFile.close()

}


// ---------------------------------------------------------------
// Photoshop utilities : Convert "charID" to "TypeID" and reversly
// ---------------------------------------------------------------
function cTID(s) {return app.charIDToTypeID(s);}
function sTID(s) {return app.stringIDToTypeID(s);}

_LFS_exportPSDLayersToPNG(); // Finaly ... execute the script
