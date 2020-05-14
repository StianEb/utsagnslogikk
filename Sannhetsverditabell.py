class Sannhetsverditabell:
    
    def __init__(self, formel):
        self._formel = formel
        self._utsagnsvariabler = sorted(list(formel.utsagnsvariabler()), key=lambda a: a.utsagnsVariabel)
        self._valuasjoner = self._genererValuasjoner(len(self._utsagnsvariabler))

    def __repr__(self):
        """Returnerer en sannhetsverditabell som en streng"""

        #Første linje av tabellen
        resultat = " | ".join([str(v) for v in self._utsagnsvariabler] + [str(self._formel)])

        #Resten av linjene
        for valuasjon in self._valuasjoner:
            resultat += "\n"
            inkludert = set([self._utsagnsvariabler[i] for i in range(len(valuasjon)) if valuasjon[i]])
            offset = " " * (len(str(self._formel))//2)
            formelVerdi = offset + ("1" if self._formel.sannVedValuasjon(inkludert) else "0")
            resultat += " | ".join([str(v) for v in valuasjon] + [formelVerdi])
            
        return "\n" + resultat

    def _genererValuasjoner(self, antVar):
        """Returnerer listen av alle mulige valuasjoner med hensyn på antall utsagnsvariabler,
hvor hver valuasjon er en liste med sannhetsverdier som knytter sannhetsverdier til utsagnsvariablene.
Eks: Hvis utsagnsvariablene er [p, q, r], så er [0, 1, 0] valuasjonen som gjør p usann, q sann og r usann."""
        
        valuasjoner = [[1]*antVar]
        for i in range(antVar):
            for element in tuple(valuasjoner):
                newElement = element.copy()
                newElement[antVar - (i + 1)] = 0
                valuasjoner.append(newElement)
        return valuasjoner
