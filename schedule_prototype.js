document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    timeZone: 'UTC',
    initialView: 'listMonth',
    eventClick: function(info) {
      var eventObj = info.event;

      if (eventObj.url) {

        window.open(eventObj.url);

        info.jsEvent.preventDefault(); // prevents browser from following link in current tab.
      } else {
        alert('Clicked ' + eventObj.title);
      }
    },
    initialDate: '2022-08-15',
    events: [
      {
        title: 'simple event',
        start: '2022-08-02'
      },
      {
        title: 'event with URL',
        url: 'https://www.google.com/',
        start: '2022-08-03'
      }
    ]
  });

  calendar.render();
});
