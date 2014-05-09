function flotFileData(file, i) {
  var reader = new FileReader();
  reader.readAsText(file);
  reader.onload = function(event){
    var csv = event.target.result;
    var data = flot2.getData();
    var newData = $.csv.toArrays(csv, {
      onParseValue:$.csv.hooks.castToScalar
    });
    // append to the existing dataset
    data[i] = newData;
    flot2.setData(data);
    flot2.setupGrid();
    flot2.draw();
  };
  reader.onerror = function(){ alert('Unable to read ' + file.fileName); };
}