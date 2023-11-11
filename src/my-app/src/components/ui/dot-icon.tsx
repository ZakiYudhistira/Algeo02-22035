import React from "react";

const DotIcon = ({ size, className }) => {
  return (
    <svg
      height={size}
      widtht={size}
      viewBox="0 0 10 10"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className={className}
    >
      <circle cx={5} cy={5} r={5} />
    </svg>
  );
};

export default DotIcon;
