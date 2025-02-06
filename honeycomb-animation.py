//start and end radius
let startRadius = 10
let endRadius = 25

//Green is set randomly for each hexagon
let myRed = 255;
let myBlue = 0;

//Honeycomb grid with information about all hexagons in the grid
//for each item (hexagon) in grid: [x, y, myGreen, radius, rotateAmount]
let grid = []

//info for each hexagon being drawn
let hexInfo = []
let hexInfos = []

function setup() {
  createCanvas(400, 400);
  
  //increments to make final hexagon grid pattern
  //not put at the top because of sqrt function
  let xIncrement = 2*endRadius*1.5
  let yIncrement = endRadius*sqrt(3)
  
  //create honeycomb hexagon grid
  honeycombGrid(0,0, xIncrement, yIncrement)
  honeycombGrid(xIncrement/2, yIncrement/2, xIncrement, yIncrement)
  
  //60 fps
  frameRate(60)
  
  //easier to navigate than radians
  angleMode(DEGREES)
}

function draw() {
  
  //select random hexagon to draw
  setTimeout( getHexInfo, 1000 )
  
  //for each hexagon added to the draw array
  for(let i = 0; i < hexInfos.length; i++) {
    
    //information for each hexagon for easy access
    let x = hexInfos[i][0]
    let y = hexInfos[i][1]
    let myGreen = hexInfos[i][2]
    let radius = hexInfos[i][3]
    let rotateAmount = hexInfos[i][4]
    
    //use frameCount as rotateAmount (60 deg per second)
    if(rotateAmount >= 0) {
      //updating array directly
      hexInfos[i][4] = frameCount
    }
    
    if(radius < endRadius) {
      //draw, rotate, and increase radius 
      //until hexagons reach proper size
      fill(color(myRed, myGreen, myBlue))
      rotateHexagon(x, y, radius, hexInfos[i][4])
      hexInfos[i][3]+=0.1
    }
    else if(360 % hexInfos[i][4] != 0) {
      //draw and rotate but keep radius the same 
      //until hexagons are properly rotated
      fill(color(myRed, myGreen, myBlue))
      rotateHexagon(x, y, radius, hexInfos[i][4])
    }
    else {
      //stop the rotation once hexagons are properly rotated
      hexInfos[i][4] = -1
    }
  }
}

function getHexInfo() {
  //until grid is empty
  if(grid.length != 0) {
    //get random hexagon from grid
    let randomIndex = int(random(0, grid.length))
    let hexInfo = grid[randomIndex]
    
    //push that hexagon to hexInfos to be drawn
    hexInfos.push(hexInfo)
    //remove that hexagon from grid so it doesn't get pushed twice
    grid.splice(randomIndex, 1)
  }
}

function rotateHexagon(x,y,radius, rotateAmount) {
  //translate to center of hexagon
  translate(x,y)
  //rotate hexagon
  rotate(rotateAmount)
  //draw hexagon
  drawHexagon(radius)
  //reset the matrix
  resetMatrix()
}

function drawHexagon(radius) {
  beginShape()
  
  //draw each vertex for a single hexagon
  for(let angle = 0; angle < 360; angle+=360/6) {
    vertex(radius*cos(angle), radius*sin(angle))
  }
  
  endShape(CLOSE)
}

function honeycombGrid(xStart, yStart, xIncrement, yIncrement) {
  //while x and y are within the canvas
  for(let x = xStart; x <= width+xIncrement; x+=xIncrement) {
    for(let y = yStart; y <= height+yIncrement; y+=yIncrement) {
      
      //set green
      let myGreen = random(140,215)
      //rotateAmount starts at 0
      let rotateAmount = 0
      
      //populate grid
      grid.push([x,y,myGreen, startRadius, rotateAmount])
    }
  }
}
