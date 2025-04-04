from rujaloxïk import Rujaloxïk
from constellationpy.client import Client

class RujaloxïkChumil(Rujaloxïk):
    def __init__(ri, chumil: Client):
        ri.chumil = chumil

    async def suivreLangues(ri):
        return await ri.chumil.bds.suivreDonnéesTableau(
            
        )
