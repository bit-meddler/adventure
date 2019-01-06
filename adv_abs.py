# prototypes for an adventure system

class AdventureGame( object ):
    def __init__(self):
        self.locations = {}
        self.loc_count = -1
        self.loc_lut   = {}
        self.items     = {}
        self.itm_count = 0
        self.itm_lut   = {}
        self.player = Player( self )
        # Room 0 is fpr deleted or sedtrpyrd items
        _ = self.createRoom( "The Void" )

    def createRoom( self, name ):
        new_room = Room( name, self )
        self.locations[ name ] = new_room
        self.loc_count += 1
        new_room.ID = self.loc_count
        self.loc_lut[ new_room.ID ] = name
        return new_room

    def createItem( self, name ):
        new_item = Item( name, self )
        self.items[ name ] = new_item
        self.itm_count += 1
        new_item.ID = self.itm_count
        self.itm_lut[ new_room.ID ] = name
        return new_item

    def play( self ):
        self.playing = True
        while( self.playing ):
            # prepare language
            curr_loc_id = self.player.location
            curr_loc_name = self.loc_lut[ curr_loc_id ]
            curr_loc = self.locations[ curr_loc_name ]

            # describe
            # room
            print( "You are {} {}.".format( curr_loc.retort() ) )
            # contents

            # exits
            print( curr_loc.getExits() )

            # get command

            # parse to verb [prep] noun [[artical] [prep2] [noun2]]

            # attempt to execute action

            
class Aobj( object ):
    def __init__( self, name, game ):
        self.name = name
        self.game = game
        self.noun = ""
        self.verb = ""
        self.syno = []
        self.ID   = -1
        # descriptions
        self.desc_short = ""
        self.desc_long  = ""


class Item( Aobj ):
    """ Item """
    def __init__( self, name, game ):
        super( Item, self ).__init__( name, game )
        self.location = -1
        self.actions = {}
        self.complaints = {}

    def moveTo( self, target ):
        new_loc  = self.game.locations[ target ]
        old_name = self.game.loc_lut[ self.location ]
        old_loc  = self.game.locations[ old_name ]
        old_loc.contents.remove( self )
        new_loc.contents.append( self )
        self.location = new_loc.ID

    def doAction( self, verb, other=None ):
        pass


class Room( Aobj ):
    """ Room """
    NAVIGATION_DIRECTIONS = ( "North", "East", "South", "West", "Up", "Down" )
    def __init__( self, name ):
        super( Room, self ).__init__( name, game )
        self.navigation  = [ None for x in self.NAVIGATION_DIRECTIONS ]
        self.contents    = []
        self.encountered = False
        self.preposition = ""

    def retort( self ):
        if( self.encountered ):
            return self.preposition, self.desc_short
        else:
            self.encountered = True
            return self.preposition, self.desc_short + ".  " + self.desc_long

    def getExits( self ):
        info = ""
        exits = []
        for i, orient in enumerate( self.NAVIGATION_DIRECTIONS ):
            if( not self.navigation[ i ] is None ):
                exits.append( orient )
        num_exits = len( exits )
        if( num_exits > 1 ):
            info = "There are exits to the {} and {}.".format( ",".join( exits[:-1] ), exits[-1] )
        elif( num_exits > 0 ):
            info = "There is an exit to the {}.".format( exits )
        else:   
            info = "No exits are visible"
        return info


class Player( Aobj ):
    """ Player """
    def __init__( self, game ):
        super( Player, self ).__init__( "Player", game )
        self.location = -1
        self.ID = -1
        self.contents = [] # inventory