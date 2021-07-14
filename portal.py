import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")


#Choose "Overworld" or "Nether" (case sensitive)
linked_portal_in = "Nether"

#Choose from portal
selected_portal = "Fountain More Y 2"

#Coord list
nether = {
    "NBase" : np.array([32, 64, -4]),
    "NMain_village" : np.array([30, 63, -21]),
    "NKI" : np.array([25, 63, -33]),
    "NCrimson_fort" : np.array([52, 63, 25]),
    "NMegabubbletea_village" : np.array([61, 63, -51]),
    "Nether_roof_fountain": np.array([26, 128, -3]),
    "Nether_roof_sword" : np.array([22, 128, -13]),


}

overworld = {
    "OKI" : np.array([211, 64, -254]),
    "OSword" : np.array([178, 71, -97]),
    "OMain_village" : np.array([260, 52, -156]),
    "OCrimson_fort" : np.array([414, 65, -199]),
    "OMegabubbletea_village" : np.array([508, 66, -430]),
    "Fountain" : np.array([215, 170, -22]),    
    "Fountain More Y" : np.array([214, 148, -7]),
    "Fountain More Y 2" : np.array([214, 148, -16]),

}

def getLinkedOverworld(netherPortal):
    portal_distances = {}

    for nname, ncoord in nether.items():    

        if (nname == netherPortal):
            overworld_coords = np.array([ncoord[0] * 8, ncoord[1], ncoord[2] * 8])
            print("Overworld coordinates for", netherPortal, ":", overworld_coords)
            for oname, ocoord in overworld.items():
                distance = np.linalg.norm(overworld_coords - ocoord)
                portal_distances[oname] = distance

    return min(portal_distances, key = portal_distances.get)

def getLinkedNether(overPortal):
    portal_distances = {}

    for oname, ocoord in overworld.items():    

        if (oname == overPortal):
            nether_coords = np.array([ocoord[0] / 8, ocoord[1], ocoord[2] / 8])
            print("Nether coordinates for", overPortal, ":", nether_coords)
            for nname, ncoord in nether.items():
                distance = np.linalg.norm(nether_coords - ncoord)
                portal_distances[nname] = distance

    return min(portal_distances, key = portal_distances.get)

#Nether to overworld
if (linked_portal_in == "Overworld"):
    linkedPortal = getLinkedOverworld(selected_portal)    
    reverseLinkedPortal = getLinkedNether(linkedPortal)
    print(selected_portal, "(Nether) links to", linkedPortal, "(Overworld)")
    print(linkedPortal, "(Overworld) links to", reverseLinkedPortal, "(Nether)")

    if (selected_portal == reverseLinkedPortal):
        print("This is a TWO way link")
    else:
        print("This is a ONE way link")

#Overworld to nether
elif (linked_portal_in == "Nether"):
    linkedPortal = getLinkedNether(selected_portal)
    print(selected_portal, "(Overworld) links to", linkedPortal, "(Nether)")
    reverseLinkedPortal = getLinkedOverworld(linkedPortal)
    print(linkedPortal, "(Nether) links to", reverseLinkedPortal, "(Overworld)")  

    if (selected_portal == reverseLinkedPortal):
        print("This is a TWO way link")
    else:
        print("This is a ONE way link")

#Error handling
else:
    print("Typo?")

