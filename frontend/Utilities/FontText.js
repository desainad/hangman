import styles from "../src/styles";
import { Text } from "react-native";
const FontText = (props) => {
  return (
    <Text style={styles.alltext} {...props}>
      {props.children}
    </Text>
  );
};
export default FontText;
