import Answer from "./Answer";

const Question = ({question}) => {
  console.log('Question', question);
  return (
    <div>
      <div className="question">{question}</div>
      <div className="answers">
        <Answer />
        <Answer />
        <Answer />
        <Answer />
      </div>
    </div>
  )
}

export default Question;