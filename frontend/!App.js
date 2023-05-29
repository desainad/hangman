import React, { useState} from "react";
import {View} from "react-native";
import { useFonts } from 'expo-font';
import FontText from "./Utilities/FontText";

export default function App() {
  const [loaded] = useFonts({
      blzee: require("./assets/fonts/blzee.ttf"),
    });
    if (!loaded) {
      return null;
    }

  return (
    <View>
      <FontText>HELLO</FontText>
      <FontText>HELLO THERE</FontText>
    </View>
  );
}
