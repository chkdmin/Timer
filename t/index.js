$(document).ready(() => {
    let start = moment('2017-03-15');
    let end = moment('2020-01-14');
    let now = moment();

    let total_days = end.diff(start, 'days');
    $('#total-days').text(total_days);

    let left_days = end.diff(now, 'days');
    $('#left-days').text(left_days);

    let total_seconds = end.diff(start, 'millisecond');
    setInterval(() => {
        let now = moment();
        let seconds = end.diff(now, 'millisecond');
        let left_percentage = (1 - (seconds / total_seconds)) * 100;
        $('#percentages').text(left_percentage.toFixed(7));

        let days = now.diff(start, 'days');
        $('#days').text(days);

        let nearly_percentages = Math.ceil(left_percentage);
        $('#nearly-percentages').text(nearly_percentages);

        let left_days_for_nearly_percentages = Math.ceil(total_days * nearly_percentages * 0.01) - days;
        $('#left-days-for-nearly-percentages').text(left_days_for_nearly_percentages);

        let floored_left_percentage = Math.floor(left_percentage);
        let next_nearly_percentages = floored_left_percentage - (floored_left_percentage % 5) + 5;
        $('#next-nearly-percentages').text(next_nearly_percentages);

        let next_nearly_percentage_days = Math.ceil(total_days * next_nearly_percentages * 0.01) - days;
        let date_for_next_nearly_percentages = now.add(next_nearly_percentage_days, 'days').format('MM/DD');
        $('#date-for-next-nearly-percentages').text(date_for_next_nearly_percentages);
    });
});
