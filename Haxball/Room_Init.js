  var roomConfig = {
      roomName : " 🦆 🦆[SPACEBOUNCE] by HonkyHost",
      playerName : "HonkyHost",
      maxPlayers : 16,
      public : true,
      token : "thr1.AAAAAGHjFKOQbxZGVzjzlg.a_wq7EcuRUo"
  };

  var stadiumFileText = `{"name":"Spacebounce Official Map","width":900,"height":550,"bg":{"type":"hockey","width":550,"height":240},"vertexes":[{"x":-550,"y":240,"cMask":["ball"]},{"x":-550,"y":80,"cMask":["ball"]},{"x":-550,"y":-80,"cMask":["ball"]},{"x":-550,"y":-240,"cMask":["ball"]},{"x":550,"y":240,"cMask":["ball"]},{"x":550,"y":80,"cMask":["ball"]},{"x":550,"y":-80,"cMask":["ball"]},{"x":550,"y":-240,"cMask":["ball"]},{"x":-1,"y":550,"bCoef":0.1,"cMask":["red","blue"],"cGroup":["redKO","blueKO"]},{"x":-1,"y":80,"bCoef":0.1,"cMask":["red","blue"],"cGroup":["redKO","blueKO"]},{"x":-1,"y":-80,"bCoef":0.1,"cMask":["red","blue"],"cGroup":["redKO","blueKO"]},{"x":-1,"y":-550,"bCoef":0.1,"cMask":["red","blue"],"cGroup":["redKO","blueKO"]},{"x":-1,"y":240,"cMask":[]},{"x":-1,"y":-240,"cMask":[]},{"x":-1,"y":80,"bCoef":0.1,"cMask":["red","blue"],"cGroup":["redKO","blueKO"]},{"x":-1,"y":-80,"bCoef":0.1,"cMask":["red","blue"],"cGroup":["redKO","blueKO"]},{"x":-547,"y":-80,"cMask":[]},{"x":-547,"y":-238,"cMask":[]},{"x":1.5,"y":-238,"cMask":[]},{"x":547,"y":-238,"cMask":[]},{"x":547,"y":-80,"cMask":[]},{"x":547,"y":80,"cMask":[]},{"x":547,"y":238,"cMask":[]},{"x":1.5,"y":238,"cMask":[]},{"x":-547,"y":238,"cMask":[]},{"x":-547,"y":80,"cMask":[]},{"x":1.5,"y":-78,"cMask":[]},{"x":1.5,"y":82,"cMask":[]}],"segments":[{"v0":16,"v1":17,"cMask":[],"color":"555555"},{"v0":17,"v1":18,"cMask":[],"color":"555555"},{"v0":18,"v1":19,"cMask":[],"color":"555555"},{"v0":19,"v1":20,"cMask":[],"color":"555555"},{"v0":20,"v1":21,"vis":false,"cMask":[],"color":"555555"},{"v0":21,"v1":22,"cMask":[],"color":"555555"},{"v0":22,"v1":23,"cMask":[],"color":"555555"},{"v0":23,"v1":24,"cMask":[],"color":"555555"},{"v0":24,"v1":25,"cMask":[],"color":"555555"},{"v0":25,"v1":16,"vis":false,"cMask":[],"color":"555555"},{"v0":18,"v1":26,"cMask":[],"color":"555555"},{"v0":26,"v1":27,"curve":179,"curveF":0.008726867790758751,"cMask":[],"color":"555555"},{"v0":27,"v1":26,"curve":-179,"curveF":-0.00872686779075885,"cMask":[],"color":"555555"},{"v0":27,"v1":23,"cMask":[],"color":"555555"},{"v0":26,"v1":27,"cMask":[],"color":"6C6C6C"},{"v0":15,"v1":14,"cMask":[],"color":"6C6C6C"},{"v0":13,"v1":15,"cMask":[],"color":"DCDCFF"},{"v0":14,"v1":12,"cMask":[],"color":"DCDCFF"},{"v0":1,"v1":2,"cMask":[],"color":"D0D0E8"},{"v0":5,"v1":6,"cMask":[],"color":"D0D0E8"},{"v0":8,"v1":9,"bCoef":0.1,"vis":false,"cMask":["red","blue"],"cGroup":["redKO","blueKO"],"color":"E0E0F8"},{"v0":9,"v1":10,"bCoef":0.1,"curve":180,"curveF":6.123233995736766e-17,"cMask":["red","blue"],"cGroup":["blueKO"],"color":"D0D0E8"},{"v0":10,"v1":9,"bCoef":0.1,"curve":180,"curveF":6.123233995736766e-17,"cMask":["red","blue"],"cGroup":["redKO"],"color":"D0D0E8"},{"v0":14,"v1":15,"bCoef":0.1,"curve":180,"curveF":6.123233995736766e-17,"cMask":["red","blue"],"cGroup":["blueKO"],"color":"D0D0E8"},{"v0":10,"v1":11,"bCoef":0.1,"vis":false,"cMask":["red","blue"],"cGroup":["redKO","blueKO"],"color":"E0E0F8"},{"v0":0,"v1":1,"bias":-100,"cMask":["ball"],"color":"D0D0E8"},{"v0":2,"v1":3,"bias":-100,"cMask":["ball"],"color":"D0D0E8"},{"v0":4,"v1":5,"bias":100,"cMask":["ball"],"color":"D0D0E8"},{"v0":6,"v1":7,"bias":100,"cMask":["ball"],"color":"D0D0E8"},{"v0":0,"v1":4,"bias":100,"cMask":["ball"],"color":"D0D0E8"},{"v0":3,"v1":7,"bias":-100,"cMask":["ball"],"color":"D0D0E8"},{"v0":1,"v1":2,"bias":-100,"bCoef":0,"curve":180,"curveF":6.123233995736766e-17,"vis":false,"cMask":["ball"],"color":"D0D0E8"},{"v0":6,"v1":5,"bias":-100,"bCoef":0,"curve":180,"curveF":6.123233995736766e-17,"vis":false,"cMask":["ball"],"color":"D0D0E8"}],"planes":[{"normal":[0,1],"dist":-550,"bCoef":0.1},{"normal":[0,-1],"dist":-550,"bCoef":0.1},{"normal":[1,0],"dist":-900,"bCoef":0.1},{"normal":[-1,0],"dist":-900,"bCoef":0.1},{"normal":[0,1],"dist":-247,"cMask":["ball"]},{"normal":[0,-1],"dist":-247,"cMask":["ball"]}],"goals":[{"p0":[-550,80],"p1":[-550,-80],"team":"red"},{"p0":[550,80],"p1":[550,-80],"team":"blue"}],"discs":[{"cGroup":["ball","kick","score"]},{"pos":[-550,80],"radius":8,"invMass":0,"color":"961515"},{"pos":[-550,-80],"radius":8,"invMass":0,"color":"961515"},{"pos":[550,80],"radius":8,"invMass":0,"color":"1E1666"},{"pos":[550,-80],"radius":8,"invMass":0,"color":"1E1666"},{"pos":[-560,78],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-570,76],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-580,74],"radius":0.01,"invMass":0,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-580,61],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-580,48],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-580,36],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-580,24],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-580,12],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-580,0],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-580,-12],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-580,-24],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-580,-36],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-580,-48],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-580,-61],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-580,-74],"radius":0.01,"invMass":0,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-570,-76],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[-560,-77],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[564,78],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[573,76],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[580,74],"radius":0.01,"invMass":0,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[580,61],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[580,48],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[580,36],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[580,24],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[580,12],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[580,0],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[580,-12],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[580,-24],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[580,-36],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[580,-48],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[580,-61],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[580,-74],"radius":0.01,"invMass":0,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[570,-76],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]},{"pos":[560,-78],"radius":0.01,"invMass":1.5,"damping":0.96,"color":"0","cMask":["ball"]}],"playerPhysics":{"bCoef":1.5,"damping":0.9995,"acceleration":0.025,"kickingAcceleration":0.0175,"kickingDamping":0.9995},"ballPhysics":"disc0","spawnDistance":350,"joints":[{"d0":1,"d1":5,"length":10.198039027185569},{"d0":5,"d1":6,"length":10.198039027185569},{"d0":6,"d1":7,"length":10.198039027185569},{"d0":7,"d1":8,"length":13},{"d0":8,"d1":9,"length":13},{"d0":9,"d1":10,"length":12},{"d0":10,"d1":11,"length":12},{"d0":11,"d1":12,"length":12},{"d0":12,"d1":13,"length":12},{"d0":13,"d1":14,"length":12},{"d0":14,"d1":15,"length":12},{"d0":15,"d1":16,"length":12},{"d0":16,"d1":17,"length":12},{"d0":17,"d1":18,"length":13},{"d0":18,"d1":19,"length":13},{"d0":19,"d1":20,"length":10.198039027185569},{"d0":20,"d1":21,"length":10.04987562112089},{"d0":21,"d1":2,"length":10.44030650891055},{"d0":3,"d1":22,"length":14.142135623730951},{"d0":22,"d1":23,"length":9.219544457292887},{"d0":23,"d1":24,"length":7.280109889280518},{"d0":24,"d1":25,"length":13},{"d0":25,"d1":26,"length":13},{"d0":26,"d1":27,"length":12},{"d0":27,"d1":28,"length":12},{"d0":28,"d1":29,"length":12},{"d0":29,"d1":30,"length":12},{"d0":30,"d1":31,"length":12},{"d0":31,"d1":32,"length":12},{"d0":32,"d1":33,"length":12},{"d0":33,"d1":34,"length":12},{"d0":34,"d1":35,"length":13},{"d0":35,"d1":36,"length":13},{"d0":36,"d1":37,"length":10.198039027185569},{"d0":37,"d1":38,"length":10.198039027185569},{"d0":38,"d1":4,"length":10.198039027185569}],"redSpawnPoints":[[-350,0],[-350,60],[-350,-60],[-350,120],[-350,-120],[-850,0]],"blueSpawnPoints":[[350,0],[350,60],[350,-60],[350,120],[350,-120],[850,0]],"kickOffReset":"full"}`;

  var room = HBInit(roomConfig);

  var players = room.getPlayerList();

  var redVictory = false;

  var blueVictory = false;

  var dynWins = 0;

  var dynRecord = 0;

  room.setCustomStadium(stadiumFileText);

  room.setTeamsLock(true);

  const inactivePlayerNames = new Set();

  const adminPlayerIDs = new Set();

  const admins = new Set();
  admins.add("Elon Stonks")
  admins.add("Mirage")
  admins.add("GeorgeParros")
  admins.add("Raamyy")
  admins.add("sasalamence")
  admins.add("Zεn")

  const blacklist = new Set();
  blacklist.add("ipooped")

  function getRandomInt(max) { // returns a random number from 0 to max-1
  return Math.floor(Math.random() * Math.floor(max - 1)+1);
  }

  room.onStadiumChange = function(stadiumName, byPlayer) {
    if(byPlayer.name != "Elon Stonks" &&  byPlayer.id != 0) {
      room.setCustomStadium(stadiumFileText);
    }
  }

  room.onPlayerJoin = function(player) {
      room.sendChat("HONK! " + "Hello, " + player.name + ". Its hard to program with webbed feet HONK! Use !help if needed HONK! ",player.id);
      // activePlayerIDs.add(player.id);
         if (blacklist.has(player.name)) {
           room.kickPlayer(player.id, "Pathetic", false);
         }
           else if (adminPlayerIDs.size == 0) {
             room.setPlayerAdmin(player.id, true);
             adminPlayerIDs.add(player.id);
             room.sendAnnouncement(player.name + "...Look at me, you're the Admin now HONK",null,0x00FF00);
           }
  //     if (adminPlayerIDs.size == 0) {
  //       room.setPlayerAdmin(player.id, true);
  //       adminPlayerIDs.add(player.id);
  //       room.sendAnnouncement(player.name + "...Look at me, you're the Admin now HONK",null,0x00FF00);
  //     }
  //       else if (blacklist.has(player.name)) {
  //         room.kickPlayer(player.id, "Pathetic", false);
  //       }
  }

  room.onPlayerChat = function(player, message) {
      var blueteam = room.getPlayerList().filter((player) => player.team == 2);
      var blueCapt = blueteam[0];
      var redteam = room.getPlayerList().filter((player) => player.team == 1);
      var redCapt = redteam[0];
      var spectators = room.getPlayerList().filter((player) => player.team == 0);
      if (message == "!topduck" && admins.has(player.name)) {
        room.setPlayerAdmin(player.id, true);
        adminPlayerIDs.add(player.id);
        return false;
      }
        else if (message == "!bb") {
          room.kickPlayer(player.id, "HONK!", false);
        }
        else if (message == "!afk" && !inactivePlayerNames.has(player.name)) {
          inactivePlayerNames.add(player.name);
          room.setPlayerTeam(player.id, 0);
          room.sendAnnouncement(player.name + " is afk!",null,0x00FF00);
        }
        else if (message == "!afk" && inactivePlayerNames.has(player.name)) {
          inactivePlayerNames.delete(player.name);
          room.sendAnnouncement(player.name + " is back!");
        }
        else if (message == "!afks") {
          room.sendAnnouncement(Array.from(inactivePlayerNames.values()) + " are AFK!",null,0x00FF00);
        }
        else if (message == "!test") {
          room.sendAnnouncement(players.name);
        }
        else if (message == "!rand" && player.name == redCapt.name && spectators.length != 1) {
          room.setPlayerTeam(spectators[getRandomInt(spectators.length)].id, player.team);
        }
        else if (message == "!rand" && player.name == blueCapt.name && spectators.length != 1) {
          room.setPlayerTeam(spectators[getRandomInt(spectators.length)].id, player.team);
        }
        else if (message == "!help") {
          room.sendChat("!admin - Become admin, message Elon on Discord @Badfoofighter#7450 to become Admin", player.id);
          room.sendChat("!afk - Mark as afk and return from afk", player.id);
          room.sendChat("!rand - Randomly pick a spectator to join your team if you are captain", player.id);
          room.sendChat("!bb - See ya, bb", player.id);
          return false;
        }
        else if (message == "!honk") {
          room.sendAnnouncement("🦆🦆",null);
        }
        else if (message == "!admin") {
          room.sendChat("Message Elon on Discord @Badfoofighter#7450 to become Admin");
        }
        else if (message == "!clearbans" && adminPlayerIDs.has(player.id)) {
          room.clearBans();
          room.sendAnnouncement("Bans have been cleared HONK!",null,0x00FF00);
        }
        else if (message == "!dyn") {
          room.sendAnnouncement("The current dynasty has won " + dynWins + " in a row",null,0x00FF00);
        }
        else {
          };
  }

  room.onPlayerKicked = function(kickedPlayer, reason, ban, byPlayer) {
    if (ban == true && !admins.has(byPlayer.name)) {
      room.sendAnnouncement(byPlayer.name + " is not authorized to ban. Clearing ban and removing their admin.",null,0xFF0000);
      room.clearBan(kickedPlayer.id);
      room.setPlayerAdmin(byPlayer.id, false);
      adminPlayerIDs.delete(player.id);
      }
      else {};
  }

  room.onPlayerTeamChange = function(player) {
    if (inactivePlayerNames.has(player.name)) {
      room.setPlayerTeam(player.id, 0);
      room.sendAnnouncement(player.name + " is afk!");
    }
  }

  room.onPlayerLeave = function(player) {
    if (inactivePlayerNames.has(player.name)) {
      inactivePlayerNames.delete(player.name);
    }
      else if (adminPlayerIDs.has(player.id)) {
        adminPlayerIDs.delete(player.id);
      }
      else{};
  }

  room.onTeamVictory = function(scores) {
    if (scores.red > scores.blue) {
      room.sendAnnouncement("Red is victorious, defeating Blue " + scores.red + "-" + scores.blue,null,0xFF0000);
      redVictory = true;
      dynWins++;
      room.sendAnnouncement("Red has won " + dynWins + " in a row!",null,0xFF0000);
      room.stopGame();
      // var blueteam = room.getPlayerList().filter((player) => player.team == 2);
      // for(var i = 0; i < blueteam.length; i++) {
      //   room.setPlayerTeam(blueteam[i].id, 0);
      }
    if (scores.blue > scores.red) {
      room.sendAnnouncement("Blue is victorious, defeating Red " + scores.blue + "-" + scores.red,null,0xFF0000);
      blueVictory = true;
      dynWins = 0
      room.stopGame();
      // var blueteam = room.getPlayerList().filter((player) => player.team == 2);
      // var redteam = room.getPlayerList().filter((player) => player.team == 1);
      // for(var i = 0; i < redteam.length; i++) {
      //   room.setPlayerTeam(redteam[i].id, 0);
      // }
      // for(var i = 0; i < blueteam.length; i++) {
      //   room.setPlayerTeam(blueteam[i].id, 1);
      // }
    }
  }

  room.onGameStart = function () {
    redVictory = false;
    blueVictory = false;
  }

  room.onGameStop = function() {
    var blueteam = room.getPlayerList().filter((player) => player.team == 2);
    var redteam = room.getPlayerList().filter((player) => player.team == 1);
    if (redVictory == true) {
      for(var i = 0; i < blueteam.length; i++) {
        room.setPlayerTeam(blueteam[i].id, 0);
      }
    }
      else if (blueVictory == true) {
        for(var i = 0; i < redteam.length; i++) {
          room.setPlayerTeam(redteam[i].id, 0);
        }
        for(var i = 0; i < blueteam.length; i++) {
          room.setPlayerTeam(blueteam[i].id, 1);
        }
    }
  }

  //ssh ec2-user@118.116.118.188 -L localhost:9222:localhost:9222 -i LightsailDefaultKey-us-east-2.pem
