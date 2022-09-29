<div>Teachable Machine Image Model - p5.js and ml5.js</div>
<script 
src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.9.0/p5.min.js"></
script>
<script 
src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.9.0/addons/p5.dom
.min.js"></script>
<script src="https://unpkg.com/ml5@latest/dist/ml5.min.js"></script>
<script type="text/javascript">
src="https://unpkg.com/ml5@latest/dist/ml5.min.js"
//For SpecialCase Robot by OzgeHulyaDurgut
let video;
let label = "Checking!";
let classifier;
let modelURL = 
'https://teachablemachine.withgoogle.com/models/MBXbP6W-9/';
//Loading the model
function preload() {
 classifier = ml5.imageClassifier(modelURL + 'model.json');
}
function setup() {
 createCanvas(500, 400);
 // Create the video
 video = createCapture(VIDEO);
 video.hide();
 // Starting classifying
 classifyVideo();
}
function classifyVideo() {
 classifier.classify(video, gotResults);
}
function draw() {
 background(0);
// Draw the video
 image(video, 0, 0);
 textSize(50);
 textAlign(CENTER, CENTER);
 fill(255);
 text(label, width / 2, height - 16);
 // Picking an emoji, the "default" is train
 let simge = "⌚";
 if (label == "Mask") {
simge = "✔";
 } else if (label == "NoMask") {
simge = "❌";
 }
 // Drawing the emoji
 textSize(50);
 text(simge, width - 30, height - 50);
}
// Getting the classification
function gotResults(error, results) {101
 if (error) {
 console.error(error);
 return;
 }
 // Storing the label and classifying again
 label = results[0].label;
 classifyVideo();
}