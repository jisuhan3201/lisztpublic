import Reactotron from 'reactotron-react-js';
import { reactotronRedux } from "reactotron-redux";

Reactotron.configure({ name: "Lisztfever"})
  .use(reactotronRedux())
  .connect();

export default Reactotron;
