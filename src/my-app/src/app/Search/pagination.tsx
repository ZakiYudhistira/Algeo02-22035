import ChevronIcon from "../../components/ui/chevron-icon";

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

  // Calculate the range of pages to display
  const displayRange = 5;
  const startPage = Math.max(
    1,
    currentNumberPage - Math.floor(displayRange / 2)
  );
  const endPage = Math.min(startPage + displayRange - 1, numberPage);

  // Create an array of numbers representing the page numbers to display
  const numbers = Array.from(
    { length: endPage - startPage + 1 },
    (_, index) => startPage + index
  );

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
      <div className="flex items-center gap-3 lg:gap-5">
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
          <div className="flex items-center">
            {numbers.map((number) => (
              <button
                key={number}
                onClick={() => setCurrentNumberPage(number)}
                aria-label={`Page-${number}`}
                className={`${
                  currentNumberPage === number && "scale-105"
                } flex items-center justify-center transition duration-300 hover:scale-125 hover:drop-shadow-[0px_0px_4px_#FFFFFF]`}
              >
                <div
                  className={`border-solid border-custom-green mx-1 px-2 py-1 ${
                    currentNumberPage === number
                      ? "bg-custom-green text-white"
                      : ""
                  }`}
                >
                  {number}
                </div>
              </button>
            ))}
          </div>
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
