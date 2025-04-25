import folium
import pandas as pd

#  Actual predictions from the API
predictions = [
   
  
   {
      "Latitude": 31.448316,
      "Longitude": 31.66321383,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4483665,
      "Longitude": 31.6634405,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44841383,
      "Longitude": 31.663665,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44845583,
      "Longitude": 31.663887,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44849533,
      "Longitude": 31.66410567,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4485325,
      "Longitude": 31.664319,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44856917,
      "Longitude": 31.66452567,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44860417,
      "Longitude": 31.66472733,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4486395,
      "Longitude": 31.66492183,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44867583,
      "Longitude": 31.6651115,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.448715,
      "Longitude": 31.66529583,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44875283,
      "Longitude": 31.66547267,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44878833,
      "Longitude": 31.66564183,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44882283,
      "Longitude": 31.66580517,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44885567,
      "Longitude": 31.665963,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44888783,
      "Longitude": 31.66611567,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.448921,
      "Longitude": 31.6662645,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.448954,
      "Longitude": 31.66640817,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.448987,
      "Longitude": 31.6665485,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44901917,
      "Longitude": 31.666684,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44904867,
      "Longitude": 31.666813,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44907767,
      "Longitude": 31.66693767,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44910583,
      "Longitude": 31.66705883,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44913317,
      "Longitude": 31.66717267,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.449158,
      "Longitude": 31.66727833,
      "Predicted Cluster": 2
    },
    {
      "Latitude": 31.44918067,
      "Longitude": 31.66737817,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.44920333,
      "Longitude": 31.66747517,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4492255,
      "Longitude": 31.66757233,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44924667,
      "Longitude": 31.66766667,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4492665,
      "Longitude": 31.66775567,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44928683,
      "Longitude": 31.66784917,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.449308,
      "Longitude": 31.667946,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44932883,
      "Longitude": 31.66804183,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44934867,
      "Longitude": 31.66813417,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.4493685,
      "Longitude": 31.668225,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.449387,
      "Longitude": 31.66831283,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44940517,
      "Longitude": 31.6683965,
      "Predicted Cluster": 2
    },
    {
      "Latitude": 31.4494225,
      "Longitude": 31.66847583,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44943833,
      "Longitude": 31.66855683,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.449455,
      "Longitude": 31.66863933,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44947367,
      "Longitude": 31.668723,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44949317,
      "Longitude": 31.668809,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4495145,
      "Longitude": 31.66890133,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44953633,
      "Longitude": 31.66899633,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44955883,
      "Longitude": 31.6690945,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44958317,
      "Longitude": 31.669193,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44960817,
      "Longitude": 31.66929383,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44963217,
      "Longitude": 31.66939683,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44965467,
      "Longitude": 31.66949383,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44967933,
      "Longitude": 31.66959917,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44970417,
      "Longitude": 31.66970317,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44972867,
      "Longitude": 31.6698085,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44975183,
      "Longitude": 31.66991517,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.449773,
      "Longitude": 31.6700165,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4497925,
      "Longitude": 31.6701185,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44981267,
      "Longitude": 31.67022067,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.449834,
      "Longitude": 31.67032233,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44985467,
      "Longitude": 31.67042233,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44987417,
      "Longitude": 31.6705175,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44989367,
      "Longitude": 31.6706105,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44991267,
      "Longitude": 31.67070033,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4499305,
      "Longitude": 31.67079,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.44994933,
      "Longitude": 31.67087967,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44996917,
      "Longitude": 31.67097233,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4499885,
      "Longitude": 31.67106567,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4500095,
      "Longitude": 31.6711615,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45002967,
      "Longitude": 31.67126067,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45004917,
      "Longitude": 31.671363,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45006833,
      "Longitude": 31.6714695,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.45008767,
      "Longitude": 31.67157583,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45010733,
      "Longitude": 31.67168367,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.45012783,
      "Longitude": 31.67179133,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4501495,
      "Longitude": 31.6718985,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45017167,
      "Longitude": 31.67200517,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.450194,
      "Longitude": 31.6721105,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.450217,
      "Longitude": 31.67221467,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45024033,
      "Longitude": 31.6723175,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45026333,
      "Longitude": 31.67241817,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45028667,
      "Longitude": 31.67251783,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45031,
      "Longitude": 31.67261617,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45033267,
      "Longitude": 31.67271317,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45035483,
      "Longitude": 31.6728085,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45037733,
      "Longitude": 31.6729035,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4503995,
      "Longitude": 31.67300117,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45042183,
      "Longitude": 31.673101,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.45044467,
      "Longitude": 31.67320167,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4504665,
      "Longitude": 31.673305,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45048833,
      "Longitude": 31.67340817,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45051,
      "Longitude": 31.67351267,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.450532,
      "Longitude": 31.67361767,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45055183,
      "Longitude": 31.6737235,
      "Predicted Cluster": 2
    },
    {
      "Latitude": 31.45057267,
      "Longitude": 31.67382917,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45059383,
      "Longitude": 31.67393633,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45061617,
      "Longitude": 31.67404417,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4506375,
      "Longitude": 31.674152,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45065933,
      "Longitude": 31.67426017,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.45068033,
      "Longitude": 31.67436833,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45070167,
      "Longitude": 31.674477,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45072317,
      "Longitude": 31.67458583,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4507445,
      "Longitude": 31.67469483,
      "Predicted Cluster": 2
    },
    {
      "Latitude": 31.4507655,
      "Longitude": 31.6748035,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.450787,
      "Longitude": 31.674913,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45080883,
      "Longitude": 31.67502183,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.45083117,
      "Longitude": 31.67513017,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45085433,
      "Longitude": 31.67523933,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.450877,
      "Longitude": 31.675348,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45090033,
      "Longitude": 31.67545617,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4509235,
      "Longitude": 31.67556367,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45094817,
      "Longitude": 31.67567017,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45097267,
      "Longitude": 31.67577733,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45099567,
      "Longitude": 31.67588417,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45101983,
      "Longitude": 31.675987,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45104267,
      "Longitude": 31.6760865,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4510655,
      "Longitude": 31.67618167,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45108667,
      "Longitude": 31.67627333,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45110683,
      "Longitude": 31.67636133,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45112517,
      "Longitude": 31.67644583,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.4511455,
      "Longitude": 31.67652283,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.451164,
      "Longitude": 31.67659833,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45118217,
      "Longitude": 31.67667217,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45119867,
      "Longitude": 31.67674367,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45121433,
      "Longitude": 31.67681567,
      "Predicted Cluster": 2
    },
    {
      "Latitude": 31.45123117,
      "Longitude": 31.67689117,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45124917,
      "Longitude": 31.67697133,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4512685,
      "Longitude": 31.67705467,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45129133,
      "Longitude": 31.67714233,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45131517,
      "Longitude": 31.67723267,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45133867,
      "Longitude": 31.6773245,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45136233,
      "Longitude": 31.67741633,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45138617,
      "Longitude": 31.67751117,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45141067,
      "Longitude": 31.6776085,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45143517,
      "Longitude": 31.67770833,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45145917,
      "Longitude": 31.67780817,
      "Predicted Cluster": 2
    },
    {
      "Latitude": 31.45148267,
      "Longitude": 31.67791167,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45150633,
      "Longitude": 31.678017,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4515325,
      "Longitude": 31.6781255,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45155533,
      "Longitude": 31.67823767,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45157883,
      "Longitude": 31.6783485,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45159933,
      "Longitude": 31.67845933,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45162417,
      "Longitude": 31.67857267,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45164933,
      "Longitude": 31.67868517,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.451674,
      "Longitude": 31.67879717,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45169983,
      "Longitude": 31.67890917,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.451726,
      "Longitude": 31.67902233,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45166817,
      "Longitude": 31.67758283,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45160933,
      "Longitude": 31.67728383,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45154933,
      "Longitude": 31.676985,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45148733,
      "Longitude": 31.67668667,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.45142433,
      "Longitude": 31.67638917,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4513595,
      "Longitude": 31.67609217,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45129333,
      "Longitude": 31.6757965,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45122567,
      "Longitude": 31.6755015,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4511585,
      "Longitude": 31.67520783,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.45109117,
      "Longitude": 31.674915,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45102333,
      "Longitude": 31.67462183,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4509565,
      "Longitude": 31.674329,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45088817,
      "Longitude": 31.67403683,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45081967,
      "Longitude": 31.67374517,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45075183,
      "Longitude": 31.6734545,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45068417,
      "Longitude": 31.67316417,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45061667,
      "Longitude": 31.67287317,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.45055133,
      "Longitude": 31.67258233,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.450487,
      "Longitude": 31.67229167,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.45042333,
      "Longitude": 31.67200117,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45036067,
      "Longitude": 31.67171033,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.450298,
      "Longitude": 31.67142083,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.4502375,
      "Longitude": 31.67113717,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45017983,
      "Longitude": 31.67086667,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.45012383,
      "Longitude": 31.67061,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45006967,
      "Longitude": 31.67036517,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.45001867,
      "Longitude": 31.6701295,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44997183,
      "Longitude": 31.6698985,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4499285,
      "Longitude": 31.66966867,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44988733,
      "Longitude": 31.66943717,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44984417,
      "Longitude": 31.66920267,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4497975,
      "Longitude": 31.6689665,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44974717,
      "Longitude": 31.668729,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.449693,
      "Longitude": 31.66848817,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.44963883,
      "Longitude": 31.66824433,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44958617,
      "Longitude": 31.667999,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44953567,
      "Longitude": 31.66775117,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44948583,
      "Longitude": 31.66750067,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44943517,
      "Longitude": 31.667246,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44938417,
      "Longitude": 31.66698783,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44933083,
      "Longitude": 31.6667275,
      "Predicted Cluster": 2
    },
    {
      "Latitude": 31.44927433,
      "Longitude": 31.66646567,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.4492155,
      "Longitude": 31.6662025,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4491555,
      "Longitude": 31.6659375,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44909667,
      "Longitude": 31.66567117,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4490355,
      "Longitude": 31.6654015,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.44897433,
      "Longitude": 31.6651305,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.4489125,
      "Longitude": 31.66485817,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44884883,
      "Longitude": 31.66458433,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44878433,
      "Longitude": 31.66431083,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44871967,
      "Longitude": 31.66403783,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44865433,
      "Longitude": 31.66376583,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44859067,
      "Longitude": 31.66349467,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44852717,
      "Longitude": 31.66322433,
      "Predicted Cluster": 3
    },
    {
      "Latitude": 31.44846133,
      "Longitude": 31.66295417,
      "Predicted Cluster": 2
    },
    {
      "Latitude": 31.448397,
      "Longitude": 31.66268517,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.448335,
      "Longitude": 31.66241633,
      "Predicted Cluster": 0
    },
    {
      "Latitude": 31.44827367,
      "Longitude": 31.66214783,
      "Predicted Cluster": 0
    }
  

]


df = pd.DataFrame(predictions)


cluster_colors = {
    0: 'green',   # Normal road
    1: 'orange',  # Speed bump
    2: 'red',     # Pothole
    3: 'p'   # Bad road
}

# Center the map at the average location
center_lat = df['Latitude'].mean()
center_lon = df['Longitude'].mean()
map_ = folium.Map(location=[center_lat, center_lon], zoom_start=15)

# Add markers for each prediction
for _, row in df.iterrows():
    cluster = row['Predicted Cluster']
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=6,
        color=cluster_colors.get(cluster, 'gray'),
        fill=True,
        fill_color=cluster_colors.get(cluster, 'gray'),
        popup=f"Cluster: {cluster}"
    ).add_to(map_)

# Save to HTML
map_.save("prediction_map.html")

print("✅ Map saved as prediction_map.html")
