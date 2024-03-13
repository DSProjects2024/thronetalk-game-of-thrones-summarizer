'''
Mock functions for testing purposes.
'''
import pandas as pd
from . import mock_constants

def mocked_read_csv_ouput_dialogues():
    """
        Mocking pandas' read_csv function for output_dialogues.
    """
    data_output_dialogues_raw = '''
,Text,Speaker,Episode,Season,Show,Episode_name,Episode_Number,Season_Number,dialogue_with_speaker
0,"[First scene opens with three Rangers riding through a tunnel, leaving the Wall, and going into the woods. (Eerie music in background) One Ranger splits off and finds a campsite full of mutilated bodies, including a child hanging from a tree branch. A birds-eye view shows the bodies arranged in a shield-like pattern. The Ranger rides back to the other two.]",NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"NARRATOR:First scene opens with three Rangers riding through a tunnel, leaving the Wall, and going into the woods. (Eerie music in background) One Ranger splits off and finds a campsite full of mutilated bodies, including a child hanging from a tree branch. A birds-eye view shows the bodies arranged in a shield-like pattern. The Ranger rides back to the other two."
1," What d’you expect? They’re savages. One lot steals a goat from another lot and before you know it, they’re ripping each other to pieces.",WAYMAR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"WAYMAR ROYCE: What d’you expect? They’re savages. One lot steals a goat from another lot and before you know it, they’re ripping each other to pieces."
2," I’ve never seen wildlings do a thing like this. I’ve never seen a thing like this, not ever in my life.",WILL,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"WILL: I’ve never seen wildlings do a thing like this. I’ve never seen a thing like this, not ever in my life."
3, How close did you get?,WAYMAR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,WAYMAR ROYCE: How close did you get?
4, Close as any man would.,WILL,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,WILL: Close as any man would.
5, We should head back to the wall.,GARED,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,GARED: We should head back to the wall.
6, Do the dead frighten you?,ROYCE,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,ROYCE: Do the dead frighten you?
7, Our orders were to track the wildlings. We tracked them. They won’t trouble us no more.,GARED,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,GARED: Our orders were to track the wildlings. We tracked them. They won’t trouble us no more.
8, You don’t think he’ll ask us how they died? Get back on your horse.,ROYCE,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,ROYCE: You don’t think he’ll ask us how they died? Get back on your horse.
9,[GARED grumbles.],NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,NARRATOR:GARED grumbles.
10, Whatever did it to them could do it to us. They even killed the children.,WILL,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,WILL: Whatever did it to them could do it to us. They even killed the children.
11," It’s a good thing we’re not children. You want to run away south, run away. Of course, they will behead you as a deserter … If I don’t catch you first. Get back on your horse. I won’t say it again.",ROYCE,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"ROYCE: It’s a good thing we’re not children. You want to run away south, run away. Of course, they will behead you as a deserter … If I don’t catch you first. Get back on your horse. I won’t say it again."
12,"[WILL glares, but obeys. Sometime later, the three Rangers return to the campsite, which is now completely cleared.]",NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"NARRATOR:WILL glares, but obeys. Sometime later, the three Rangers return to the campsite, which is now completely cleared."
13, Your dead men seem to have moved camp.,ROYCE,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,ROYCE: Your dead men seem to have moved camp.
14, They were here.,WILL,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,WILL: They were here.
15, See where they went.,GARED,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,GARED: See where they went.
16,"[The three look around, swords drawn. They hear the wind and eerie calls. GARED finds a red cloth in the snow.]",NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"NARRATOR:The three look around, swords drawn. They hear the wind and eerie calls. GARED finds a red cloth in the snow."
17, What is it?,ROYCE,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,ROYCE: What is it?
18, It’s …,GARED,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,GARED: It’s …
19,"[As he speaks, a CREATURE with glowing blue eyes rises behind ROYCE. ROYCE turns, the CREATURE strikes. The scene shifts to WILL, who hears a man crying out. The three horses stampede past him. He turns and sees someone standing very still in the distance. The figure turns – it’s the child who had been suspended in the tree, now with glowing blue eyes. WILL turns and runs.",NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"NARRATOR:As he speaks, a CREATURE with glowing blue eyes rises behind ROYCE. ROYCE turns, the CREATURE strikes. The scene shifts to WILL, who hears a man crying out. The three horses stampede past him. He turns and sees someone standing very still in the distance. The figure turns – it’s the child who had been suspended in the tree, now with glowing blue eyes. WILL turns and runs."
20,"GARED is also fleeing, and we hear strange growls and catch glimpses of the CREATURE. Both terrified RANGERS stop, some distance apart, to catch their breath. WILL sees a CREATURE behead GARED. WILL sinks to his knees and the CREATURE tosses GARED’S head to him.]",NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"NARRATOR:GARED is also fleeing, and we hear strange growls and catch glimpses of the CREATURE. Both terrified RANGERS stop, some distance apart, to catch their breath. WILL sees a CREATURE behead GARED. WILL sinks to his knees and the CREATURE tosses GARED’S head to him."
21,[Blackout],NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,NARRATOR:Blackout
22,"TITLE SEQUENCE[Riders from Winterfell come up behind a dazed WILL. The scene shifts to the castle, where BRAN is practicing archery and getting frustrated, under the eyes of JON SNOW and ROBB STARK. JON pats BRAN’S shoulder.]",NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"NARRATOR:TITLE SEQUENCERiders from Winterfell come up behind a dazed WILL. The scene shifts to the castle, where BRAN is practicing archery and getting frustrated, under the eyes of JON SNOW and ROBB STARK. JON pats BRAN’S shoulder."
23, Go on. Father’s watching.,JON,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,JON: Go on. Father’s watching.
24,[We see NED and CATELYN STARK watching from above.],NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,NARRATOR:We see NED and CATELYN STARK watching from above.
25, And your mother.,JON,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,JON: And your mother.
26,[Scene shifts to needlework practice with the girls inside the castle.],NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,NARRATOR:Scene shifts to needlework practice with the girls inside the castle.
27," Fine work, as always. Well done.",SEPTA,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"SEPTA MORDANE (to SANSA): Fine work, as always. Well done."
28, Thank you.,SANSA,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,SANSA: Thank you.
29, I love the detail that you’ve managed to get in this corners. … Quite beautiful … the stitching …,SEPTA,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,SEPTA MORDANE: I love the detail that you’ve managed to get in this corners. … Quite beautiful … the stitching …
30,"[As she murmurs to SANSA about the embroidery, ARYA struggles with her needlework and listens to the arrows hitting and the male laughter outside.]",NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"NARRATOR:As she murmurs to SANSA about the embroidery, ARYA struggles with her needlework and listens to the arrows hitting and the male laughter outside."
31,"[Outside, BRAN tries and misses again. Everyone laughs.]",NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"NARRATOR:Outside, BRAN tries and misses again. Everyone laughs."
32," And which one of you was a marksman at ten? Keep practicing, Bran. Go on.",NED,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"NED: And which one of you was a marksman at ten? Keep practicing, Bran. Go on."
33," Don’t think too much, Bran.",JON,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"JON: Don’t think too much, Bran."
34, Relax your bow arm.,ROBB,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,ROBB: Relax your bow arm.
35,"[BRAN pulls the arrow back. An arrow hits the bullseye. BRAN (still with his arrow), JON, and ROBB turn in surprise to see ARYA, who curtsies after her perfect shot. ROBB and JON laugh as Bran takes out after ARYA.]",NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"NARRATOR:BRAN pulls the arrow back. An arrow hits the bullseye. BRAN (still with his arrow), JON, and ROBB turn in surprise to see ARYA, who curtsies after her perfect shot. ROBB and JON laugh as Bran takes out after ARYA."
36," Quick, Bran, faster!",JON/ROBB,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,"JON/ROBB: Quick, Bran, faster!"
37,[RODRICK CASSEL and THEON GREYJOY approach NED and CATELYN on the balcony.],NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,NARRATOR:RODRICK CASSEL and THEON GREYJOY approach NED and CATELYN on the balcony.
38, Lord Stark. My lady. A guardsman just rode in from the hills. They’ve captured a deserter from the Night’s Watch.,CASSEL,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,CASSEL: Lord Stark. My lady. A guardsman just rode in from the hills. They’ve captured a deserter from the Night’s Watch.
39,[NED grimaces.],NARRATOR,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,NARRATOR:NED grimaces.
40, Get the lads to saddle their horses.,NED,e1,season-01,Game-of-Thrones,Winter is Coming,1,1,NED: Get the lads to saddle their horses.
    '''
    lines = data_output_dialogues_raw.splitlines()
    data = [line.split(',') for line in lines[1:]]
    dataframe = pd.DataFrame(data[1:], columns=data[0])
    # mock_output_dialogues_raw = pd.read_csv(StringIO(data_output_dialogues_raw))
    return dataframe

# *args is required to catch arguments passed while using with
# unittest's @patch, disabling the pylint warning.
# pylint: disable=unused-argument
def mock_model_azure_api_call(*args):
    '''Mocks the response of azure_api_call from model.py's Model class.'''
    return mock_constants.CHAT_COMPLETIONS_MOCK_RESPONSE
