from django.shortcuts import render

from busstations.models import Station, Route


def view_stations(request):
    routes_list = Route.objects.all()
    template_name = 'stations.html'
    route = request.GET.get('route')
    if route:
        target_route = Station.objects.filter(routes__name=route)
        for station in target_route:
            print(station.name, station.longitude, station.latitude)
        context = {'routes': routes_list, 'stations': target_route}
    if not route:
        context = {'routes': routes_list}
    return render(request, template_name, context)
