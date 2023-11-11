import ChevronIcon from "./chevron-icon";
import DotIcon from "./dot-icon";

const Pagination = ({
  numberPage,
  currentNumberPage,
  setCurrentNumberPage,
  previousButton = false,
  nextButton = false,
  primaryColor,
}) => {
  // Define color effects based on the primary color provided
  const colorEffect = {
    pink: { selected: "fill-[#DF3890]", unselected: "fill-[#7A2F8B]" },
  };

  // Create an array of numbers representing the page numbers
  const numbers = Array.from({ length: numberPage }, (_, index) => index + 1);

  // Handle previous page button click
  const handlePreviousClick = () => {
    const newPage = ((currentNumberPage - 2 + numberPage) % numberPage) + 1;
    setCurrentNumberPage(newPage);
  };

  // Handle next page button click
  const handleNextClick = () => {
    const newPage = (currentNumberPage % numberPage) + 1;
    setCurrentNumberPage(newPage);
  };

  // Return the pagination UI
  return (
    // Display pagination only if there's more than one page
    numberPage > 1 && (
      <div className="flex gap-3 lg:gap-5">
        {/* Display previous page button if enabled */}
        {previousButton && (
          <button
            onClick={handlePreviousClick}
            aria-label="Previous Button"
            className={`px-2 transition duration-300 hover:scale-125 hover:drop-shadow-[0px_0px_4px_#FFFFFF]`}
          >
            <ChevronIcon className="stroke-white rotate-180 w-[15px] h-[15px] lg:w-[20px] lg:h-[20px]" />
          </button>
        )}
        <div className="flex gap-2 lg:gap-4">
          {/* Map through page numbers and display dots */}
          {numbers.map((number) => (
            <button
              key={number}
              onClick={() => setCurrentNumberPage(number)}
              aria-label={`Page-${number}`}
              className={`${
                currentNumberPage === number && "scale-105"
              } transition duration-300 hover:scale-125 hover:drop-shadow-[0px_0px_4px_#FFFFFF]`}
            >
              <DotIcon
                size={12}
                className={`${
                  currentNumberPage === number
                    ? colorEffect[primaryColor].selected
                    : colorEffect[primaryColor].unselected
                } w-[8px] lg:w-[17px]`}
              />
            </button>
          ))}
        </div>
        {/* Display next page button if enabled */}
        {nextButton && (
          <button
            onClick={handleNextClick}
            aria-label="Next Button"
            className={`px-2 transition duration-300 hover:scale-125 hover:drop-shadow-[0px_0px_4px_#FFFFFF]`}
          >
            <ChevronIcon className="stroke-white w-[15px] h-[15px] lg:w-[20px] lg:h-[20px]" />
          </button>
        )}
      </div>
    )
  );
};
export default Pagination;
