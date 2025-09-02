import React from 'react';

const buttons = [
  { name: "Buy1", category: "Buy/Sell" },
  { name: "Sell1", category: "Buy/Sell" },
  { name: "TrigTime", category: "Timeframe" },
  { name: "TF1", category: "Timeframe" },
  { name: "TF2", category: "Timeframe" },
  { name: "TF3", category: "Timeframe" },
  { name: "TF4", category: "Timeframe" },
  { name: "TF5", category: "Timeframe" },
  { name: "TrigCont", category: "Amount" },
  { name: "IncAmt", category: "Amount" },
  { name: "DecAmt", category: "Amount" },
  { name: "TrigSig", category: "Signal" },
  { name: "SearchSig", category: "Signal" },
  { name: "ConfTrade", category: "Signal" }
];

function FloatingBar() {
  return (
    <div className="floating-bar">
      {buttons.map(btn => (
        <div key={btn.name} className="floating-btn-container">
          <button className="round-btn" aria-label={btn.name}></button>
          <div className="btn-label">{btn.name}</div>
        </div>
      ))}
    </div>
  );
}

export default FloatingBar;
