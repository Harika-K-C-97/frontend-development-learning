import { useReducer } from "react";
import Question from "./Question";

const initialState = {
  currentQuestionIndex: 0,
  questions: [],
  answers: [],
}

const reducer = (state, action) => {
  switch (action.type) {
    case 'NEXT_QUESTION':
      return {
        ...state,
        currentQuestionIndex: state.currentQuestionIndex + 1
      };
    default:
      return state;
  }
}

const Quiz = () => {

  const [state, dispatch] = useReducer(reducer, initialState);
  console.log('render', state);

  return (
    <div className="quiz">
      <div>
        <div className="score">Question {state.currentQuestionIndex}/8</div>
        <Question question={state.questions[state.currentQuestionIndex] } />
        <div className="next-button" onClick={() => dispatch({ type: 'NEXT_QUESTION' })}>Next Question</div>
      </div>
    </div>
  )
}

export default Quiz;