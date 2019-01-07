#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import string

class Parser( object ):
    def __init__( self, nouns, noun_syns, verbs, verb_syns ):
        self.nouns = nouns
        self.noun_syns = noun_syns
        self.verbs = verbs
        self.verb_syns = verb_syns

        # substitution dicts
        self.noun_tree = {}
        self.verb_tree = {}

        # build trees
        self.prepNouns()
        self.prepVerbs()

        # transtab
        self._cleaner = r"!\"£$%^&*()_+-=,./?|[]@';:<>"

    @staticmethod
    def _buildTreeD( tree, subs_dict ):
        for word, syns in subs_dict.iteritems():
            x_word = word.replace( " ", "_" )
            for syn in syns:
                Parser._add2Tree( tree, x_word, syn )

    @staticmethod
    def _buildTreeL( tree, sub_list ):
        for words in sub_list:
            x_word = words.replace( " ", "_" )
            Parser._add2Tree( tree, x_word, words )

    @staticmethod
    def _add2Tree( tree, target, words ):
        t = tree
        parts = words.split()
        for part in parts:
            if( not part in t ):
                t[ part ] = {}
            t = t[ part ]
        t["Terminus"] = target

    def prepNouns( self ):
        self._buildTreeD( self.noun_tree, self.noun_syns )
        self._buildTreeL( self.noun_tree, self.nouns )

    def prepVerbs( self ):
        pass

    def cleanupInput( self, text ):
        ret = text.lower()
        ret = string.translate( ret, None, self._cleaner )
        return ret


# words need to be simple, so synons reeduce complex clauses to simple words
# two word terms need to be contracted to a single block (with underscores?)
verbs = ["get", "look", "open", "put", "plant"]
verb_synons = {
    "get"   : ["take", "pick up",],
    "look"  : ["examine"],
    "plant" : ["bury"],
}
nouns = ["key", "door", "plant pot", "pot plant", "house key", "house cat", "pick axe"]
noun_synons = {
    "pick axe"  : ["pick", "axe"],
    "house cat" : ["cat"],
    "pot plant" : ["plant"],
    "plant pot" : ["pot"],
}

P = Parser( nouns, noun_synons, verbs, verb_synons )
print( P.cleanupInput( "'Pull my finger!' said Bevis, with an evil glint in his eye." ) )
print( P.noun_tree )