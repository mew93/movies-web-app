
function showHide(ElementID) {
	if (arguments.length === 1){
	    var x = document.getElementById(ElementID);
	    if (x.style.display === 'none') {
	        x.style.display = 'block';
	    } else if (x.style.display === 'block') {
	        x.style.display = 'none';
	    } else {
	    	x.style.display = 'block';
	    }
	}
	if (arguments.length === 0) {
	    var x = document.getElementsByClassName('hidden');
    	for (i=0; i< x.length; i++){
	    if (x[i].style.display === 'none') {
	        x[i].style.display = 'block';
	    } else if (x[i].style.display === 'block') {
	        x[i].style.display = 'none';
	    } else {
	    	x[i].style.display = 'block';
	    }
	}
	}
}