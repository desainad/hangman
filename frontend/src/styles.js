// styles.js

import {StyleSheet, Dimensions } from "react-native";
import {keys} from "./constants";

const screenWidth = Dimensions.get("window").width;
const keyWidth = (screenWidth - 10) / keys[0].length;
const keyHeight = keyWidth * 1.3;

export default StyleSheet.create({
  alltext: {
    fontFamily: "Playfulist",
  },
  image: {
    width: "100%",
    height: "100%",
    margin: (55, 5, 5, 5),
  },
  container: {
    display: "flex",
    flexDirection: "row",
    width: "100%",
    height: "15%",
    textAlign: "center",
    justifyContent: "center",
  },
  titleView: {
    margin: (0, 0, 0, 24),
  },
  titleText: {
    fontFamily: "Playfulist",
    color: "#fff",
    fontSize: 24,
  },
  container2: {
    flexDirection: "row",
    margin: 5,
    height: "45%",
  },
  imageContainer: {
    flexDirection: "column",
    flex: 1,
    width: "35%",
    margin: 2,
  },
  hmImage: {
    justifyContent: "flex-start",
  },
  wordContainer: {
    flexDirection: "column",
    width: "65%",
    alignItems: "stretch",
    justifyContent: "space-around",
    margin: 1,
  },
  wordText: {
    flexWrap: "wrap",
    margin: 2,
    fontSize: 32,
    color: "#fff",
    fontFamily: "Playfulist",
  },

  container3: {
    flexDirection: "column",
    height: "35%",
    margin: 5,
  },
  keyboardContainer: {
    flexDirection: "row",
    justifyContent: "space-around",
    margin: 5,
  },
  row: {
    flexDirection: "row",
    justifyContent: "center",
  },
  letterButton: {
    width: keyWidth - 5,
    height: keyHeight - 20,
    margin: 0,
    borderRadius: 5,
    alignItems: "center",
    justifyContent: "center",
  },
  letterText: {
    fontFamily: "Playfulist",
    fontSize: 24,
  },
  triesContainer: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    margin: 15,
  },
  triesText: {
    fontSize: 20,
    color: "#fff",
    fontFamily: "Playfulist",
  },

  buttonContainer: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
  },
  button: {
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "transparent",
    borderRadius: 8,
    padding: 5,
    height: 40,
    borderWidth: 1,
    borderColor: "green",
    color: "#fff",
  },
  circleGradient: {
    margin: 1,
    backgroundColor: "white",
    borderRadius: 5,
  },
  visit: {
    margin: 4,
    paddingHorizontal: 6,
    textAlign: "center",
    backgroundColor: "white",
    color: "#008f68",
    fontSize: 12,
  },
});
