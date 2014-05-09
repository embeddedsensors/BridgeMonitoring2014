function flotTextData() {
  var options = {
    series: {
      lines: { show: true },
    }
  };
  var data1 = [];
  data1[0] = jQuery.csv.toArrays($('#NWdata').val(), {
    onParseValue: jQuery.csv.hooks.castToScalar
  });
  flot1 = jQuery.plot(jQuery('#plotholder'), data1, options);
  jQuery("#textP").attr("text","hello");
}