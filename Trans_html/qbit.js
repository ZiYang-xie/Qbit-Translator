var button = document.getElementsByClassName("audio")[0];
var audio = document.getElementById("player"); 
var state = false;
button.onclick = function audio_play(){
    button.className = 'button audio-onclick';
    if(state){ //如果是播放
        audio.pause();
        audio.currentTime = 0;
        button.className = 'button audio';
        state = false;
        
    }else{ //如果是暂停
        audio.play()
        state = true;
    }
    audio.onended = function(){
        button.className = 'button audio';
    }
}