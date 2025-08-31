

function formatDateString(date){

    const newDate = new Date(date);

    const formattedDate = newDate.toLocaleDateString("en-US", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit"
    });

    const formattedTime = newDate.toLocaleTimeString("en-US", {
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: false,     
        timeZoneName: "short"
    });

    return `${formattedDate} ${formattedTime}`;
}

export default formatDateString;
