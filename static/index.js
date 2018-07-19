$(document).ready(() => {
    let start = moment('2017-03-15');
    let end = moment('2020-01-14');

    let total_seconds = end.diff(start, 'millisecond');
    setInterval(() => {
        let now = moment();
        let seconds = end.diff(now, 'millisecond');
        let left_percentage = (1 - (seconds / total_seconds)) * 100;
        $('#percentages').text(left_percentage.toFixed(7));
    });
});
