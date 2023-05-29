import React, { useState, useEffect } from "react";
import { View, Pressable, ImageBackground, TouchableOpacity } from "react-native";
import { LinearGradient } from "expo-linear-gradient";
import styles from './src/styles';
import {colors, keys} from './src/constants';
import Hm1svg from './assets/animations/hm_1.svg';
import Hm2svg from "./assets/animations/hm_2.svg";
import Hm3svg from "./assets/animations/hm_3.svg";
import Hm4svg from "./assets/animations/hm_4.svg";
import Hm5svg from "./assets/animations/hm_5.svg";
import Hm6svg from "./assets/animations/hm_6.svg";
import Hm7svg from "./assets/animations/hm_7.svg";
import { useFonts } from 'expo-font';
import FontText from "./Utilities/FontText";

const MAX_TRIES = 6;

export default function App() {
  const [selectedWord, setSelectedWord] = useState("");
  const [guessedLetters, setGuessedLetters] = useState([]);
  const [wrongTries, setWrongTries] = useState(0);
  const [newGamePressed, setNewGamePressed] = useState(false);
  wordSelected = false
  
  // Set up a new game when the component mounts
  useEffect(() => {
    setUpNewGame();
  }, []);

  // Check if the game is over (win or lose) whenever the guessedLetters or wrongTries change
  useEffect(() => {
    if (newGamePressed) {
      setNewGamePressed(false)
      setUpNewGame()
    } else if (wrongTries >= MAX_TRIES) {
      hangmanAnimation()
      alert(`Game over! The word was "${selectedWord}".`);
    } else if (
        !getGuessedWord().includes("-")  
         && selectedWord.length>0) {
            alert("Congratulations, you won!");
        }
  }, [guessedLetters, wrongTries, newGamePressed]);

  // Set up a new game by selecting a random word and resetting state variables
  const setUpNewGame = () => {
    setSelectedWord("")
    console.log('in new game')
    wordSelected = getMovies()
    if (wordSelected) {
        console.log("selected word is" + selectedWord);
    }
    else {
        console.log("selected word not found");
    }
    setGuessedLetters([]);
    setWrongTries(0);
  }

  async function getMovies() {
    API_HOST = "http://10.0.2.2:8000/hangman/api/movies";
    console.log('in getMovies')
    try {
      const response = await fetch(API_HOST, { method: "GET" });
      const jsonData = await response.json();
      console.log(jsonData.toUpperCase());
      setSelectedWord(jsonData.toUpperCase());
      return true
    } catch (error) {
      console.error("Error", error);
      return false;
    }
  }

  // Handle a letter being guessed
  const handleGuessLetter = (letter) => {
    setGuessedLetters([...guessedLetters, letter]);
    if (!selectedWord.includes(letter) ) {
      setWrongTries(wrongTries + 1);
    }
  };

  // Get the word to display, with underscores for unguessed letters
  const getGuessedWord = () => {
    var stringGuessedWord = ""
    selectedWord.split("").map((letter) => {
      if (letter === " " || letter === "'" || letter === "-") {
        stringGuessedWord = stringGuessedWord + letter;
      } else if (guessedLetters.includes(letter) === false) {
        stringGuessedWord = stringGuessedWord + "-";
      } else {
        stringGuessedWord = stringGuessedWord + letter;
      } 
    })
    stringGuessedWord.toUpperCase();
    return stringGuessedWord;
    
  };

  // Generate buttons for each letter of the alphabet
  const getKeyColor = (key) => {
    if (!guessedLetters.includes(key)) {
        return colors.primary;
     }
    else if (guessedLetters.includes(key) &&
              selectedWord.indexOf(key) >= 0) {
                  return colors.green;
              }
    else return colors.secondary

  }
  const KeyboardView = () => {
    return (
      <View>
        {keys.map((keyRow, i) => (
          <View style={styles.row} key={`row-${i}`}>
            {keyRow.map((key) => (
              <Pressable
                onPress={() => handleGuessLetter(key)}
                disabled={guessedLetters.includes(key)}
                key={key}
                style={[styles.letterButton, { color: getKeyColor(key) }]}
              >
                <View>
                  <LinearGradient
                    colors={["#C00000", "#EE0000", "#CC0066"]}
                    style={styles.button}
                  >
                    <FontText style={[styles.letterText]}>{key}</FontText>
                  </LinearGradient>
                </View>
              </Pressable>
            ))}
          </View>
        ))}
      </View>
    );
 }
  
  const hangmanAnimation = () => {
    switch (wrongTries) {
      case 1:
        return <Hm2svg style={styles.hmImage}/>;
      case 2:
        return <Hm3svg style={styles.hmImage} />;
      case 3:
        return <Hm4svg style={styles.hmImage} />;
      case 4:
        return <Hm5svg style={styles.hmImage} />;
      case 5:
        return <Hm6svg style={styles.hmImage} />;
      case 6:
        return <Hm7svg style={styles.hmImage} />;
      default:
        return <Hm1svg style={styles.hmImage} />;
    }}

  const [loaded] = useFonts({
    Playfulist: require("./assets/fonts/Playfulist.otf"),
  });

  if (!loaded) {
    return null;
  }
  return (
    <View>
      <ImageBackground
        style={styles.image}
        source={require("./assets/images/HM_RPChalkboard.jpg")}
      >
        <View style={styles.container}>
          <View style={styles.titleView}>
            <FontText style={styles.titleText}>HangMan (Movies)</FontText>
          </View>
        </View>

        <View style={styles.container2}>
          <View style={styles.imageContainer}>{hangmanAnimation()}</View>
          <View style={styles.wordContainer}>
            <FontText style={styles.wordText}>{getGuessedWord()}</FontText>
          </View>
        </View>

        <View style={styles.container3}>
          <View style={styles.keyboardContainer}>
            <KeyboardView />
          </View>
          <View style={styles.triesContainer}>
            <FontText
              style={styles.triesText}
            >{`Wrong Tries: ${wrongTries}`}</FontText>
          </View>
          <View style={styles.buttonContainer}>
            <TouchableOpacity
              style={styles.button}
              onPress={() => setNewGamePressed(true)}
            >
              <FontText style={styles.triesText}>New Game</FontText>
            </TouchableOpacity>
          </View>
        </View>
      </ImageBackground>
    </View>
  );
}
