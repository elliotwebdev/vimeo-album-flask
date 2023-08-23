var video01Player;
var $videoSrc; 

/*jQuery */
$(document).ready(function() {
  console.log("ready!");
  
  // Gallery mouse events:
  $(".figure").css("cursor", "pointer");

  /* Close buttton for nav overlay, will unload and destroy player */
  $(".closebtn").click(function(){
    video01Player.unload().then(function(){
      //video was unloaded
    }).catch(function(error) {
      //error occurred
    });
    video01Player.destroy();
    document.getElementById("myNav").style.width = "0%";
  });

  /* Load player function, retrieves url corresponding to its element*/
  $(".video-btn").click(function(){
      $videoSrc = $(this).data( "src" );
      console.log($videoSrc);

    var options01 = {
      url: $videoSrc,
      width:800
    };

    video01Player = new Vimeo.Player("Vimeo_Player", options01);

    video01Player.setVolume(1);

    video01Player.on('play', function() {
      console.log('Played the first video');
    });
    document.getElementById("myNav").style.width = "100%";
  });
});