from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import Http404
from django.http import HttpResponse
from models import SampleMessage
from msgint.segment import textseg

def msg_list(request):
    title = 'Sample Message Collection'
    array = SampleMessage.objects.order_by('-id')
    count = array.count()
    return render_to_response('msg_list.html', locals())

def msg_spam(request):
    title = 'Spam Message Collection'
    array = SampleMessage.objects.filter(tag = '*').order_by('-id')
    count = array.count()
    return render_to_response('msg_list.html', locals())

def msg_normal(request):
    title = 'Normal Message Collection'
    array = SampleMessage.objects.filter(tag = '+').order_by('-id')
    count = array.count()
    return render_to_response('msg_list.html', locals())

def msg_add(request):
    errors = []
    if request.method == 'POST':
        c = request.POST.get('content', '')
        t = request.POST.get('tag')
        if not c:
            errors.append('Please enter message content.')
        if not t:
            errors.append('Please select message category.')
        if not errors:
            msg = SampleMessage(content = c, tag = t)
            msg.update_content_digest()
            old = SampleMessage.objects.filter(digest = msg.digest).count()
            if old > 0:
                errors.append('Message exists.')
            else:
                msg.save()
                return HttpResponseRedirect('/')
    return render_to_response('msg_add.html', {'errors': errors})

def msg_del(request):
    if request.method == 'POST':
        p = request.POST.get('id')
        if p:
            k = int(p)
            SampleMessage.objects.filter(id = k).delete()
            return HttpResponse('')
    raise Http404

def msg_seg(request, pk):
    d = int(pk)
    msg = SampleMessage.objects.get(id = d)
    text = msg.content.encode('utf-8')
    seg_smallseg = textseg.seg_smallseg(text)
    seg_scws = textseg.seg_scws(text)
    #seg_pymmseg = textseg.seg_pymmseg(text)
    return render_to_response('msg_seg.html', {'content': text, 'smallseg': seg_smallseg, 'scws': seg_scws})
    