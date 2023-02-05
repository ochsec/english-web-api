import React, { useState } from 'react';

export default Request = (props) => {
    const [text, setText] = useState('');
  
    const handleChange = (e) => {
      setText(e.target.value);
    };
  
    const handleSubmit = (e) => {
      e.preventDefault();
      console.log('You submitted the text "' + text + '"');
    };
  
    return (
      <form onSubmit={handleSubmit} className="measure center">
        <textarea
          value={text}
          onChange={handleChange}
          className="db border-box hover-black w-100 measure ba b--black-20 pa2 br2 mb2"
        ></textarea>
        <small 
          className="f6 black-60">
            Enter your plain text request here.
        </small>
        <input 
          type="submit" 
          value="Submit" 
          className='f6 grow no-underline br-pill ba ph3 pv2 mb2 dib dark-green' />
      </form>
    );
  }