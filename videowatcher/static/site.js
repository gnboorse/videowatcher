//site.js
var myinterval = 1000;
var maxdx = 3;
var myPlayer = videojs("sessionplayer");
var previousTime = myPlayer.currentTime();

function postupdate(session_id, time, is_paused)
{
    console.log(JSON.stringify({"time": time, "is_paused": is_paused}));
    var dataString = '{"time":' + time.toString() + ', "is_paused":' + is_paused.toString() + '}';
     $.ajax
    ({
        type: "POST",
        url: "/session_handle/" + session_id,
        dataType: "text",
        contentType: "application/json",
        data: dataString,
        success: function () {
            //alert("Thanks!");
            console.log('Updated session (time = ' + time.toString() + ', ispaused = ' + is_paused.toString() + ')');

        },
        error: function(jqXHR, textStatus, errorThrown){
            console.log('HTTP error: ' + textStatus + ', ' + errorThrown);
        }

    });
}

function callUpdate(session_id)
{
    $.getJSON("/session_handle/" + session_id.toString(),
    function(json)
    {
        var currentTime = myPlayer.currentTime();
         //if success:

        var time = json.time;
        var is_paused = json.is_paused;
        var px = Math.abs(previousTime - currentTime);
        var qx = Math.abs(time - currentTime);
        var dx = Math.abs( px - qx );
        console.log(' - Got session data (time = ' + time.toString() + ', ispaused = ' + is_paused.toString() + '), dx = ' + dx.toString());

        if (dx > maxdx)
        {
            myPlayer.currentTime(time);
        }

        if (is_paused != myPlayer.paused())
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


        previousTime = currentTime;
    });
}

function setEvents(session_id) 
{
    
    callUpdate(session_id);


    myPlayer.on('pause', function()
    {
        // console.log('paused');
        postupdate(session_id, myPlayer.currentTime(), is_paused=true);
    });


    myPlayer.on('play', function()
    {
        // console.log('played');
        postupdate(session_id, myPlayer.currentTime(), is_paused=false);
    });

    myPlayer.on('timeupdate', function()
    {   
        $.getJSON("/session_handle/" + session_id.toString(),
            function(json)
            {

                //if success:
                var currentTime = myPlayer.currentTime();
                 //if success:

                var time = json.time;
                var is_paused = json.is_paused;
                var px = Math.abs(previousTime - currentTime);
                var qx = Math.abs(time - currentTime);
                var dx = Math.abs( px - qx );
                // console.log('interval call (' + is_paused.toString() + ', ' + time.toString() + ')');
                if (dx > maxdx)
                {
                     postupdate(session_id, myPlayer.currentTime(), is_paused=is_paused);
                }
            });
    });

    setInterval(function()
    {
       callUpdate(session_id);

    },  myinterval);

}