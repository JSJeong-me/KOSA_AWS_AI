"use strict";

const serverUrl = "http://static-web-me.s3-website-ap-northeast-1.amazonaws.com/api";

function runDemo() {
    fetch(serverUrl + "/demo-object-detection", {
        method: "GET"
    }).then(response => {
        if (!response.ok) {
            throw response;
        }
        return response.json();
    }).then(data => {
        let imageElem = document.getElementById("image");
        imageElem.src = data.imageUrl;
        imageElem.alt = data.imageName;
        let objectsElem = document.getElementById("objects");
        let objects = data.objects;
        for (let i = 0; i < objects.length; i++) {
            let labelElem = document.createElement("h6");
            labelElem.appendChild(document.createTextNode(
                objects[i].label + ": " + objects[i].confidence + "%")
            );
            objectsElem.appendChild(document.createElement("hr"));
            objectsElem.appendChild(labelElem);
        }
    }).catch(error => {
        alert("Error: " + error);
    });
}

