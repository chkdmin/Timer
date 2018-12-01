$(document).ready(() => {
    let start = moment(START_DATE_STRING);
    let end = moment(END_DATE_STRING);

    let total_seconds = end.diff(start, 'millisecond');
    setInterval(() => {
        let now = moment();
        let seconds = end.diff(now, 'millisecond');
        let left_percentage = (1 - (seconds / total_seconds)) * 100;
        $('#current-percentages').text(left_percentage.toFixed(7));
    });

    $('.toggle').click((e) => {
        const $box = $(e.target).parents('.toggle-box').children('div');
        if ($box.css('display') == 'none') {
            $box.show();
        } else {
            $box.hide();
        }
    })
});
