var displayNames = [];
var dropZone = document.getElementById("drop-zone");
var fileList = document.getElementById("file-list");
var formatSelect = document.getElementById("format-select");

document.addEventListener("dragover", function (e) { e.preventDefault(); });
document.addEventListener("drop", function (e) { e.preventDefault(); });

dropZone.addEventListener("dragover", function (e) {
  e.preventDefault();
  dropZone.classList.add("drag-over");
});

dropZone.addEventListener("dragleave", function () {
  dropZone.classList.remove("drag-over");
});

dropZone.addEventListener("drop", function (e) {
  e.preventDefault();
  dropZone.classList.remove("drag-over");

  var files = Array.from(e.dataTransfer.files);
  if (files.length === 0) return;

  var paths = files.map(function (f) { return f.path; }).filter(Boolean);

  if (paths.length === files.length) {
    pywebview.api.add_paths(paths).then(function (names) {
      displayNames = displayNames.concat(names);
      renderList();
    });
  } else {
    var reads = files.map(function (file) {
      return new Promise(function (resolve) {
        var reader = new FileReader();
        reader.onload = function () {
          resolve({ name: file.name, data: reader.result });
        };
        reader.readAsDataURL(file);
      });
    });
    Promise.all(reads).then(function (fileData) {
      pywebview.api.add_files_data(fileData).then(function (names) {
        displayNames = displayNames.concat(names);
        renderList();
      });
    });
  }
});

document.getElementById("btn-select").addEventListener("click", function () {
  pywebview.api.select_images().then(function (names) {
    displayNames = displayNames.concat(names);
    renderList();
  });
});

document.getElementById("btn-convert").addEventListener("click", function () {
  var format = formatSelect.value;
  pywebview.api.convert(format).then(function (res) {
    if (res.ok) {
      displayNames = [];
      renderList();
    }
    alert(res.msg);
  });
});

document.getElementById("btn-clear").addEventListener("click", function () {
  pywebview.api.clear_list().then(function () {
    displayNames = [];
    renderList();
  });
});

function renderList() {
  fileList.innerHTML = displayNames
    .map(function (n) {
      return "<li>" + escapeHtml(n) + "</li>";
    })
    .join("");
}

function escapeHtml(str) {
  var div = document.createElement("div");
  div.appendChild(document.createTextNode(str));
  return div.innerHTML;
}
