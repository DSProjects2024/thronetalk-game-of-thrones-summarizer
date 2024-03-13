'''
Mock functions for testing purposes.
'''
import pandas as pd
from . import mock_constants

# *args is required to catch arguments passed while using with
# unittest's @patch, disabling the pylint warning.
# pylint: disable=unused-argument
def mocked_read_csv_ouput_dialogues(*args):
    """
    Mock for pandas' read_csv function for output_dialogues.
    """
    mock_rows = [
        ["First scene opens with three Rangers riding through a tunnel, leaving the Wall, and going into the woods. (Eerie music in background) One Ranger splits off and finds a campsite full of mutilated bodies, including a child hanging from a tree branch. A birds-eye view shows the bodies arranged in a shield-like pattern. The Ranger rides back to the other two.','narrator','e1','season-01','Game-of-Thrones','Winter is Coming",1,1,"NARRATOR:First scene opens with three Rangers riding through a tunnel, leaving the Wall, and going into the woods. (Eerie music in background) One Ranger splits off and finds a campsite full of mutilated bodies, including a child hanging from a tree branch. A birds-eye view shows the bodies arranged in a shield-like pattern. The Ranger rides back to the other two."],
        ["What d’you expect? They’re savages. One lot steals a goat from another lot and before you know it, they’re ripping each other to pieces.",'waymar','e1','season-01','Game-of-Thrones','Winter is Coming',1,1,"WAYMAR ROYCE: What d’you expect? They’re savages. One lot steals a goat from another lot and before you know it, they’re ripping each other to pieces."],
        ["I’ve never seen wildlings do a thing like this. I’ve never seen a thing like this, not ever in my life.",'will','e1','season-01','Game-of-Thrones','Winter is Coming',1,1,"WILL: I’ve never seen wildlings do a thing like this. I’ve never seen a thing like this, not ever in my life."],
        ['How close did you get?','waymar','e1','season-01','Game-of-Thrones','Winter is Coming',1,1,'WAYMAR ROYCE: How close did you get?'],
        ['Close as any man would.','will','e1','season-01','Game-of-Thrones','Winter is Coming',1,1,'WILL: Close as any man would.'],
        ["We should head back to the wall.", "gared", "e1", "season-01", "Game-of-Thrones", "Winter is Coming", 1, 1, "GARED: We should head back to the wall."],
        ["Do the dead frighten you?", "royce", "e1", "season-01", "Game-of-Thrones", "Winter is Coming", 1, 1, "ROYCE: Do the dead frighten you?"],
        ["Our orders were to track the wildlings. We tracked them. They won’t trouble us no more.", "gared", "e1", "season-01", "Game-of-Thrones", "Winter is Coming", 1, 1, "GARED: Our orders were to track the wildlings. We tracked them. They won’t trouble us no more."],
        ["You don’t think he’ll ask us how they died? Get back on your horse.", "royce", "e1", "season-01", "Game-of-Thrones", "Winter is Coming", 1, 1, "ROYCE: You don’t think he’ll ask us how they died? Get back on your horse."],
        ["[GARED grumbles.]", "narrator", "e1", "season-01", "Game-of-Thrones", "Winter is Coming", 1, 1, "NARRATOR:GARED grumbles."],
        ["Whatever did it to them could do it to us. They even killed the children.", "will", "e1", "season-01", "Game-of-Thrones", "Winter is Coming", 1, 1, "WILL: Whatever did it to them could do it to us. They even killed the children."],
        ["It’s a good thing we’re not children. You want to run away south, run away. Of course, they will behead you as a deserter … If I don’t catch you first. Get back on your horse. I won’t say it again.", "royce", "e1", "season-01", "Game-of-Thrones", "Winter is Coming", 1, 1, "ROYCE: It’s a good thing we’re not children. You want to run away south, run away. Of course, they will behead you as a deserter … If I don’t catch you first. Get back on your horse. I won’t say it again."],
        ["[WILL glares, but obeys. Sometime later, the three Rangers return to the campsite, which is now completely cleared.]", "narrator", "e1", "season-01", "Game-of-Thrones", "Winter is Coming", 1, 1, "NARRATOR:WILL glares, but obeys. Sometime later, the three Rangers return to the campsite, which is now completely cleared."],
        ["Your dead men seem to have moved camp.", "royce", "e1", "season-01", "Game-of-Thrones", "Winter is Coming", 1, 1, "ROYCE: Your dead men seem to have moved camp."],
        ["They were here.", "will", "e1", "season-01", "Game-of-Thrones", "Winter is Coming", 1, 1, "WILL: They were here."],
        ["See where they went.", "gared", "e1", "season-01", "Game-of-Thrones", "Winter is Coming", 1, 1, "GARED: See where they went."],
        ["[The three look around, swords drawn. They hear the wind and eerie calls. GARED finds a red cloth in the snow.]", "narrator", "e1", "season-01", "Game-of-Thrones", "Winter is Coming", 1, 1, "NARRATOR:The three look around, swords drawn. They hear the wind and eerie calls. GARED finds a red cloth in the snow."],
        ["What is it?", "royce", "e1", "season-01", "Game-of-Thrones", "Winter is Coming", 1, 1, "ROYCE: What is it?"],
        ["It's...", "gared", "e1", "season-01", "Game-of-Thrones", "", 1, 1, "GARED: It's...", "gared"],
        ["", "narrator", "e1", "season-01", "Game-of-Thrones", "", 1, 1, "NARRATOR: As he speaks, a CREATURE with glowing blue eyes rises behind ROYCE. ROYCE turns, the CREATURE strikes. The scene shifts to WILL, who hears a man crying out. The three horses stampede past him. He turns and sees someone standing very still in the distance. The figure turns – it's the child who had been suspended in the tree, now with glowing blue eyes. WILL turns and runs.", "narrator"],
        ["", "narrator", "e1", "season-01", "Game-of-Thrones", "", 1, 1, "NARRATOR: GARED is also fleeing, and we hear strange growls and catch glimpses of the CREATURE. Both terrified RANGERS stop, some distance apart, to catch their breath. WILL sees a CREATURE behead GARED. WILL sinks to his knees and the CREATURE tosses GARED'S head to him.", "narrator"],
        ["", "narrator", "e1", "season-01", "Game-of-Thrones", "", 1, 1, "NARRATOR: Blackout", "narrator"],
        ["", "narrator", "e1", "season-01", "Game-of-Thrones", "", 1, 1, "NARRATOR: TITLE SEQUENCE Riders from Winterfell come up behind a dazed WILL. The scene shifts to the castle, where BRAN is practicing archery and getting frustrated, under the eyes of JON SNOW and ROBB STARK. JON pats BRAN'S shoulder.", "narrator"],
        ["Go on. Father's watching.", "jon", "e1", "season-01", "Game-of-Thrones", "", 1, 1, "JON: Go on. Father's watching.", "jon snow"],
        ["", "narrator", "e1", "season-01", "Game-of-Thrones", "", 1, 1, "NARRATOR: We see NED and CATELYN STARK watching from above.", "narrator"],
        ["And your mother.", "jon", "e1", "season-01", "Game-of-Thrones", "", 1, 1, "JON: And your mother.", "jon snow"],
    ]
    columns = [
        'Text','Speaker','Episode','Season','Show','Episode_name',
        'Episode_Number','Season_Number','dialogue_with_speaker','Character'
    ]
    dataframe = pd.DataFrame(mock_rows, columns=columns)
    return dataframe

# pylint: disable=unused-argument
def mock_model_azure_api_call(*args):
    '''Mocks the response of azure_api_call from model.py's Model class.'''
    return mock_constants.CHAT_COMPLETIONS_MOCK_RESPONSE
