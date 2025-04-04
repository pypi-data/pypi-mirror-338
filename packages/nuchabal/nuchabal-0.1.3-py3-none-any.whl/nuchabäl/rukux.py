import json
import os
import unicodedata
from importlib import resources
from typing import Optional

from .rujaloxïk import Rujaloxïk


def _rujaqik_json(wuj):
    with open(wuj, encoding='utf8') as w:
        return json.load(w)


class Nuchabäl(object):
    rkxnkNklm = {
        "glottologue": "gl",
        "iso1": "i1",
        "iso2": "i2",
        "iso3": "i3"
    }

    def __init__(ri, rujaloxïk: Optional[Rujaloxïk] = None):
        cholajibäl_retamabäl = resources.files("nuchabäl.retamabäl")
        ri.retamabälChabäl = _rujaqik_json(cholajibäl_retamabäl.joinpath("ch'ab'äl.json"))
        ri.retamabälTzibanem = _rujaqik_json(cholajibäl_retamabäl.joinpath("tzib'.json"))

        ri.rujaloxïk = rujaloxïk

    def konojelChabäl(ri):
        return list(ri.retamabälChabäl)

    def konojelTzibanem(ri):
        return list(ri.retamabälTzibanem)

    def runukChabäl(ri, chabäl: str, runukulem: Optional[str]) -> Optional[str]:
        try:
            rnkNchbl = next(rnk for rnk in ri.retamabälChabäl.keys() if ri.retamabälTzibanem[rnk]["rb'"] == chabäl)
        except StopIteration:
            return

        if runukulem is None:
            return rnkNchbl
        runukulem = runukulem.lower()
        taqrunuk = ri.retamabälChabäl[rnkNchbl].rn
        if runukulem == 'iso':
            for i in range(1, 4):
                if rnk := f"i{i}" in taqrunuk:
                    return taqrunuk[rnk]
        return taqrunuk[ri.rkxnkNklm[runukulem]]

    def rubiChabäl(ri, runuk: str, runukulem: Optional[str]) -> Optional[str]:
        runukulem = (runukulem or "").lower()
        if runukulem in ri.rkxnkNklm:
            try:
                rtmbl = next(
                    x for x in ri.retamabälChabäl.values() if runukulem in x["rn"] and x["rn"][runukulem] == runuk)
            except StopIteration:
                return
        elif runukulem == '':
            rtmbl = ri.retamabälChabäl[runuk]
        elif runukulem == 'iso':
            rtmbl = next((
                r for r in ri.retamabälChabäl.values()
                if any(r["rn"][x] == runuk for x in ["i1", "i2", "i3"] if x in r["rn"])
            ), None)
        else:
            rtmbl = None
        return rtmbl["rb'"] if rtmbl else None

    def rutzibChabäl(ri, runuk: str) -> Optional[str]:
        if runuk in ri.retamabälChabäl:
            rtmbl = ri.retamabälChabäl[runuk]
            if rtmbl and "tz" in rtmbl:
                return rtmbl["tz"]

    def rajilanïkChabäl(ri, runuk: str) -> Optional[str]:
        if runuk in ri.runukChabäl:
            rtmbl = ri.retamabälChabäl[runuk]
            if "aj" in rtmbl:
                return rtmbl["aj"]

        runukTzib = ri.rutzibChabäl(runuk)
        return ri.rajilanïkTzibanem(runukTzib)

    def rubiTzibanem(ri, runuk: str) -> Optional[str]:
        if runuk in ri.retamabälTzibanem:
            rtmbl = ri.retamabälTzibanem[runuk]
            if "rb'" in rtmbl:
                return rtmbl["rb'"]

    def rucholanemTzibanem(ri, runuk: str) -> Optional[str]:
        rtmbl = ri.retamabälTzibanem[runuk]
        if rtmbl:
            return rtmbl.ch
        rtmbl_iso = unicodedata.bidirectional(runuk[0])
        return "→↓" if rtmbl_iso == "L" else "←↓"

    def rajilanïkTzibanem(ri, runuk):
        if runuk in ri.retamabälTzibanem:
            rtmbl = ri.retamabälTzibanem[runuk]
            if "aj" in rtmbl:
                return rtmbl["aj"]


nuchabäl = Nuchabäl()
