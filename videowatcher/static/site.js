//site.js
//javascript to handle automatic update of video playback
function videoloop(session_id)
{
    $.get("/session_handle/" + session_id,
        function(data)
        {
            console.log(data);
            //if success:
            var json_obj = JSON.parse(data.responseText);

            var time = json_obj.time;
            var is_paused = json_obj.is_paused;

            var myPlayer = videojs("sessionplayer"); //this is the playback object

            if (myPlayer.paused() != is_paused)
            {
                //we have to set it
                if (is_paused)
                {
                    myPlayer.pause();
                    console.log('paused the player');
                }
                else
                {
                    myPlayer.play();
                    console.log('started the player');
                }
            }

            if (myPlayer.currentTime() != time)
            {
                myPlayer.currentTime(time);
            }
        }
    )


}

function postupdate(session_id, time, is_paused)
{
     $.ajax
    ({
        type: "POST",
        url: "/session_handle/" + session_id,
        dataType: "json",
        data: JSON.stringify({"time": time, "is_paused": is_paused}),
        success: function () {
            //alert("Thanks!");
            console.log('Updated session (time = ' + time.toString() + ', ispaused = ' + is_paused.toString() + ')');

        }

    });
}
