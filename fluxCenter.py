from Vector2D import Vector2D
def fluxCenter(list_of_points: Vector2D):
    #f docstring
    """
    This function computes the center of mass of a polygon specified by its verticies.
    """
    #d
    #f helper functions!
    def areaFlux(point_1,point_2): #f
        return(0.5*(point_1.y-point_2.y)*(point_1.x+point_2.x)) #d
    def momentFluxX(point_1,point_2): #f
        return(
            (1/6)*
            (point_1.y-point_2.y)*
            (
                point_1.x*point_1.x+
                point_2.x*point_2.x+
                point_1.x*point_2.x
            )
        ) #d
    def momentFluxY(point_1,point_2): #f
        return(
            (1/6)*
            (point_2.x-point_1.x)*
            (
                point_1.y*point_1.y+
                point_2.y*point_2.y+
                point_1.y*point_2.y
            )
        ) #d
    #d
    #f initialize variables!
    total_area_flux=0
    total_moment_flux_x=0
    total_moment_flux_y=0
    #d
    #f sum the flux!
    #f add flux of every line except the last one!
    for i in range(len(list_of_points)-1):
       total_area_flux += areaFlux(list_of_points[i],list_of_points[i+1]) 
       total_moment_flux_x += momentFluxX(list_of_points[i],list_of_points[i+1]) 
       total_moment_flux_y += momentFluxY(list_of_points[i],list_of_points[i+1]) 
    #d
    #f add the flux of the last line!
    firstpoint = list_of_points[0]
    lastpoint = list_of_points[len(list_of_points)-1]
    total_area_flux += areaFlux(lastpoint,firstpoint) 
    total_moment_flux_x += momentFluxX(lastpoint,firstpoint) 
    total_moment_flux_y += momentFluxY(lastpoint,firstpoint) 
    #d
    #d
    #f compute the center of mass!
    center_of_mass_x = total_moment_flux_x/total_area_flux
    center_of_mass_y = total_moment_flux_y/total_area_flux
    center_of_mass_vector = Vector2D(center_of_mass_x,center_of_mass_y)
    #d
    return(center_of_mass_vector)
