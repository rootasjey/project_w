// JAVASCRIPT FOR PROJECT REPORT
// -----------------------------
// WEBAPP
// -----------------------------

// ----------------------
// RELOAD THE IFRAME PAGE
function reload_iframe(event) {
	var parent = event.target.parentNode;
	var frame = parent.firstElementChild;
	var src = frame.src;
	frame.src = src;
}