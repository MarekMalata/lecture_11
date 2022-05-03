import matplotlib.pyplot as plt

def flood_fill(obraz, x, y):
    if x < 0 or x >= obraz.shape[1] or y < 0 or y >= obraz.shape[0]:
        return obraz
    if obraz[y,x] == 2 or obraz[y,x] == 0:
        return obraz

    obraz[y,x] = 2
    obraz = flood_fill(obraz, x+1, y)
    obraz = flood_fill(obraz, x-1, y)
    obraz = flood_fill(obraz, x, y+1)
    obraz = flood_fill(obraz, x, y-1)

    plt.imshow(obraz, cmap="gray")
    plt.show(block=False)
    plt.pause(0.01)
    plt.clf()

    return obraz





def main():
    img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    # img = floodfill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()

    flood_fill(img, 0, 0)

   # print(flood_fill(img, 0, 0))

if __name__ == "__main__":
    main()
