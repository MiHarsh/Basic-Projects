var gamePattern = [];
var userClickedPattern = [];
var buttonColours = ["red","blue","green","yellow"]; 
var level = 0;
var started = false;

function nextSequence(){
    var randomNumber = Math.floor(Math.random() * 4) ;
    var randomChosenColour = buttonColours[randomNumber];
    gamePattern.push(randomChosenColour);
    level+=1;
    $("#level-title").text("Level "+level);
}



function playAudio(color){
    var audio = new Audio("sounds/"+color+".mp3");
    audio.play();
}





$(".btn").click(function() {

    var userChosenColour = $(this).attr("id");
    userClickedPattern.push(userChosenColour);
    playAudio(userChosenColour);
    $("#"+userChosenColour).fadeOut(100).fadeIn(100).fadeOut(100).fadeIn(100);
    animatePress(userChosenColour);
  });

function animatePress(currentColor) {
    $("#" + currentColor).addClass("pressed");
    setTimeout(function () {
      $("#" + currentColor).removeClass("pressed");
    }, 100);
  }

$(document).keypress(function(event){
    if(started !== true){
    nextSequence();}
    started = true;
  })