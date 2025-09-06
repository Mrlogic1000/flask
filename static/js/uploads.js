const dropArea = document.getElementById('drop-area')
const fileInput = document.getElementById('input-file')
const imageView = document.getElementById('img-view')



fileInput.addEventListener("change",uploadImage)

function uploadImage(){
    let imgLink = URL.createObjectURL(fileInput.files[0]);
    imageView.style.backgroundImage = `url(${imgLink})`;
    imageView.textContent = "";
    imageView.style.border = 0;
}

dropArea.addEventListener("dragover", function(e){
    e.preventDefault();
});
 dropArea.addEventListener("drop", function(e){
    e.preventDefault();
    fileInput.files = e.dataTransfer.files;
    uploadImage();
 })