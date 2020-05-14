#Credit: This file borrows many elements from a library by Robin Wellner.
#Check it out on GitHub: https://gist.github.com/gvx/2185287

from Sannhetsverditabell import Sannhetsverditabell
import itertools

class Formel:
    def __neg__(self): # Operator: -
        return Negasjon(self)
    def __and__(self, other): # Operator: &
        return Konjunksjon(self, other)
    def __or__(self, other): # Operator: |
        return Disjunksjon(self, other)
    def __gt__(self, other): # Operator: >
        return Implikasjon(self, other)
    def __xor__(self, other): # Operator: ^
        return DobbelImplikasjon(self, other)
    def __mod__(self, other): # Operator: %
        return DobbelImplikasjon(self, other).erTautologi() ## Ekvivalens!
    
    def sannhetsverditabell(self):
        return Sannhetsverditabell(self)
    
    def erTautologi(self):
        uv = list(self.utsagnsvariabler())
        valuasjoner = list(itertools.product([1, 0], repeat=len(uv)))
        for valuasjon in valuasjoner:
            inkludert = set([uv[i] for i in range(len(valuasjon)) if valuasjon[i]])
            if not self.sannVedValuasjon(inkludert):
                return False
        return True
    
    def erKontradiksjon(self):
        uv = list(self.utsagnsvariabler())
        valuasjoner = list(itertools.product([1, 0], repeat=len(uv)))
        for valuasjon in valuasjoner:
            inkludert = set([uv[i] for i in range(len(valuasjon)) if valuasjon[i]])
            if self.sannVedValuasjon(inkludert):
                return False
        return True
            

class Atom(Formel):
    def __init__(self, utsagnsVariabel):
        self.utsagnsVariabel = utsagnsVariabel
    def __repr__(self):
        return self.utsagnsVariabel
    def sannVedValuasjon(self, valuasjon):
        return self in valuasjon
    def utsagnsvariabler(self):
        return {self}

class Top(Formel):
    def __repr__(self):
        return '⊤'
    def sannVedValuasjon(self, valuasjon):
        return True
    def utsagnsvariabler(self):
        return set()

class Bot(Formel):
    def __repr__(self):
        return '⊥'
    def sannVedValuasjon(self, valuasjon):
        return False
    def utsagnsvariabler(self):
        return set()

class UnaerFormel(Formel):
    def __init__(self, barn):
        self.barn = barn
    def __repr__(self):
        return self.symbol + str(self.barn)
    def utsagnsvariabler(self):
        return self.barn.utsagnsvariabler()

class BinaerFormel(Formel):
    def __init__(self, venstre, hoeyre):
        self.venstre = venstre
        self.hoeyre = hoeyre
    def __repr__(self):
        return '(' + str(self.venstre) + ' ' + self.symbol + ' ' + str(self.hoeyre) + ')'
    def utsagnsvariabler(self):
        return self.venstre.utsagnsvariabler() | self.hoeyre.utsagnsvariabler()

class Negasjon(UnaerFormel):
    symbol = '¬'
    def sannVedValuasjon(self, valuasjon):
        return not self.barn.sannVedValuasjon(valuasjon)
    
class Konjunksjon(BinaerFormel):
    symbol = '∧'
    def sannVedValuasjon(self, valuasjon):
        return self.venstre.sannVedValuasjon(valuasjon) and self.hoeyre.sannVedValuasjon(valuasjon)

class Disjunksjon(BinaerFormel):
    symbol = '∨'
    def sannVedValuasjon(self, valuasjon):
        return self.venstre.sannVedValuasjon(valuasjon) or self.hoeyre.sannVedValuasjon(valuasjon)

class Implikasjon(BinaerFormel):
    symbol = '→'
    def sannVedValuasjon(self, valuasjon):
        return not self.venstre.sannVedValuasjon(valuasjon) or self.hoeyre.sannVedValuasjon(valuasjon)

class DobbelImplikasjon(BinaerFormel):
    symbol = '↔'
    def sannVedValuasjon(self, valuasjon):
        return self.venstre.sannVedValuasjon(valuasjon) == self.hoeyre.sannVedValuasjon(valuasjon)
    
