
H = polytopes.hypercube(4, intervals='zero_one')

def stuff(H, M):
    pos = [f for f in H.faces(2) if 
           all(ray.vector()*vector((1,1,1,1))>0 for ray in f.normal_cone().rays())]
    neg = [f for f in H.faces(2) if 
           all(ray.vector()*vector((1,1,1,1))<0 for ray in f.normal_cone().rays())]

    A = PolyhedronPartition([M.change_ring(RDF) * f.as_polyhedron() for f in pos]).plot()
    B = PolyhedronPartition([M.change_ring(RDF) * f.as_polyhedron() for f in neg]).plot()


