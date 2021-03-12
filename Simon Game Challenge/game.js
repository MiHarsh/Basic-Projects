var gamePattern = [];
var userClickedPattern = [];
var buttonColours = ["red","blue","green","yellow"]; 
var level = 0;
var started = false;

// generate sequence
function nextSequence(){
    userClickedPattern = [];
    var randomNumber = Math.floor(Math.random() * 4) ; // randomNumber ranging 0 to 3
    var randomChosenColour = buttonColours[randomNumber]; // color corresponding index
    gamePattern.push(randomChosenColour);
    level+=1; //increase the level
    $("#level-title").text("Level " + level);
    playAudio(randomChosenColour);
    $("#"+randomChosenColour).fadeOut(100).fadeIn(100).fadeOut(100).fadeIn(100);
}

// to play audio corresponding to the color
function playAudio(color){
    var audio = new Audio("sounds/"+color+".mp3");
    audio.play();
}

// add eventListener, activates when any button is clicked
$(".btn").click(function() {
    var userChosenColour = $(this).attr("id");
    userClickedPattern.push(userChosenColour);
    playAudio(userChosenColour);
    $("#"+userChosenColour).fadeOut(100).fadeIn(100).fadeOut(100).fadeIn(100);
    animatePress(userChosenColour);
    checkAnswer(userClickedPattern.length-1);
  });

// show the current keyPress
function animatePress(currentColor) {
    $("#" + currentColor).addClass("pressed");
    setTimeout(function () {
      $("#" + currentColor).removeClass("pressed");
    }, 100);
  }

// added keypress eventListener (To start the Game)
$(document).keypress(function() {
  if (!started) {
    $("#level-title").text("Level " + level);
    nextSequence();
    started = true;
  }
});

// checkAnswer on each level, if wrong restart the game
function checkAnswer(currentLevel){
  if(gamePattern[currentLevel]===userClickedPattern[currentLevel]){
    if (userClickedPattern.length === gamePattern.length){
      setTimeout(function () {
        nextSequence();
      }, 1000);
    }
  }
  else{
    playAudio("wrong");
    $("body").addClass("game-over");
    setTimeout(function () {
      $("body").removeClass("game-over");
    }, 200);
    $("h1").text("Game Over, Press Any Key to Restart");
    startOver();
  }
}

// reset everything on game restart
function startOver(){
  level = 0;
  gamePattern = [];
  started = false;
}