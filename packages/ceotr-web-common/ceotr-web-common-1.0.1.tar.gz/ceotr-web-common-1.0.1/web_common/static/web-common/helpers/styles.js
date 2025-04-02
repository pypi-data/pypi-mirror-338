/**
 * Distinct colour list to display many overlapping coloured lines (leaflet map), etc.
 * @type {{distinctList: string[], print: Window.ColorPalette.print}}
 */
window.ColorPalette = {

	// Source: https://graphicdesign.stackexchange.com/questions/3682/where-can-i-find-a-large-palette-set-of-contrasting-colors-for-coloring-many-d
	distinctList: [
		"rgb(1,0,103)",
		"rgb(255,0,86)",
		"rgb(158,0,142)",
		"rgb(14,76,161)",
		"rgb(0,95,57)",
		"rgb(0,255,0)",
		"rgb(149,0,58)",
		"rgb(255,147,126)",
		"rgb(164,36,0)",
		"rgb(0,21,68)",
		"rgb(98,14,0)",
		"rgb(107,104,130)",
		"rgb(0,0,255)",
		"rgb(0,125,181)",
		"rgb(106,130,108)",
		"rgb(0,174,126)",
		"rgb(194,140,159)",
		"rgb(190,153,112)",
		"rgb(0,143,156)",
		"rgb(95,173,78)",
		"rgb(255,0,0)",
		"rgb(255,0,246)",
		"rgb(255,2,157)",
		"rgb(104,61,59)",
		"rgb(255,116,163)",
		"rgb(150,138,232)",
		"rgb(167,87,64)",
		"rgb(1,255,254)",
		"rgb(254,137,0)",
		"rgb(1,208,255)",
		"rgb(187,136,0)",
		"rgb(117,68,177)",
		"rgb(255,166,254)",
		"rgb(119,77,0)",
		"rgb(122,71,130)",
		"rgb(38,52,0)",
		"rgb(0,71,84)",
		"rgb(67,0,44)",
		"rgb(181,0,255)",
		"rgb(126,45,210)",
		"rgb(189,211,147)",
		"rgb(229,111,254)",
		"rgb(0,255,120)",
		"rgb(0,155,255)",
		"rgb(0,100,1)",
		"rgb(0,118,255)",
		"rgb(133,169,0)",
		"rgb(0,185,23)",
		"rgb(120,130,49)",
		"rgb(0,255,198)",
		"rgb(255,110,65)",
		"rgb(232,94,190)",
		"rgb(0,0,0)",
	],
	print: function() {
		console.log("ColorPalette.distinctColors: ");
		ColorPalette.distinctList.forEach(function(val) {
			console.log("%c " + val, "background-color: " + val + ";");
		});
	}

};