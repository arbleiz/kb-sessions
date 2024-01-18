from ninja import NinjaAPI

ninja_api = NinjaAPI()


@ninja_api.get("/tunes")
def tunes(request):
    return {"tunes": [
            {
                "name": "The Road To Lisdoonvarna",
                "rythm": "slide",
                "key": "Em",
                "links": [
                    {
                        "label": "TheSession.org",
                        "url": "https://thesession.org/tunes/250",
                    }
                ],
            }
        ]
    }