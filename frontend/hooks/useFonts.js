import * as Font from "expo-font";

const useFonts = async () =>
  await Font.loadAsync({
    "Playfulist": require("../assets/fonts/Playfulist.otf"),
    "blzee": require("../assets/fonts/blzee.ttf"),
    "ComicNeue-Bold": require("../assets/fonts/ComicNeue-Bold.ttf"),
    "ComicNeue-BoldItalic": require("../assets/fonts/ComicNeue-BoldItalic.ttf"),
    "ComicNeue-Italic": require("../assets/fonts/ComicNeue-Italic.ttf"),
    "ComicNeue-Light": require("../assets/fonts/ComicNeue-Light.ttf"),
    "ComicNeue-LightItalic": require("../assets/fonts/ComicNeue-LightItalic.ttf"),
    "ComicNeue-Regular": require("../assets/fonts/ComicNeue-Regular.ttf"),
  });
  export default useFonts;
