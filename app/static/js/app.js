"use strict";

let selectedFile = document.getElementById("file");

// On change of file input element we want to grab the selected File name
// place it in inside <p> element
if (selectedFile) {
    selectedFile.addEventListener("change", function (event) {
        // split the filename on basis of '\' this and select last one
        let selectedFileText = event.target.value.split('\\').pop();

        if (selectedFileText) {
            if (selectedFileText.length > 30) {
                selectedFileText = selectedFileText.substring(0, 30) + "....";
            }
            let selSpan = document.getElementsByClassName("sel-file");
            selSpan[0].textContent = 'Selected File: ' + selectedFileText;
        }

    });
}

let flashMsgs = document.getElementsByClassName('flash-msg');
if (flashMsgs) {
    for (let i = 0; i < flashMsgs.length; ++i) {
        flashMsgs[i].addEventListener('click', function(event) {
            if (event.type === 'click') {
                this.className += " silenter";
            }
        }, true);
    }
}

let copyBtn = document.querySelector('.copyBtn');
if (copyBtn) {
    copyBtn.addEventListener('click', function() {
        let text = document.querySelector('.textToCopy').href;
        window.prompt('Ctrl-c and Enter', text);
    });
}