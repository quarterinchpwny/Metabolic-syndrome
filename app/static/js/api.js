$(document).ready(function(e) {

    $('#makePred').click(function() {

        $('#hfProb').empty();
        $('#hfPred').empty();

        var sex = $('#sex').val();
        var Age = $('#age').val();
        var Marital = $('#Marital').val();
        var Income = $('#Income').val();
        var Race = $('#Race').val();
        var WaistCirc = $('#WaistCirc').val();
        var BMI = $('#BMI').val();
        var Albuminuria = $('#Albuminuria').val();
        var UrAlbCr = $('#UrAlbCr').val();
        var BloodGlucose = $('#BloodGlucose').val();
        var HDL = $('#HDL').val();
        var Triglycerides = $('#Triglycerides').val();
        var UricAcid = $('#UricAcid').val();

        var inputData = {
            'sex': sex,
            'Marital': Marital,
            'Income': Income,
            'Race': Race,
            'WaistCirc': WaistCirc,
            'Age': Age,
            'BMI': BMI,
            'Albuminuria': Albuminuria,
            'UrAlbCr': UrAlbCr, 
            'UricAcid': UricAcid,
            'BloodGlucose': BloodGlucose,
            'HDL': HDL,
            'Triglycerides':Triglycerides
        };

        $.ajax({
            url: 'main/api/make_prediction',
            data: inputData,
            type: 'post',
            success: function(response) {
                $('#main').hide()
                $('#result').show()
                console.log(response);

                $('#tdSex').append('<p >'+$('#sex').val()+'</p>');
                $('#tdAge').append('<p >'+$('#age').val()+'</p>');
                $('#tdMarital').append('<p>'+$('#Marital').val()+'</p>');
                $('#tdIncome').append('<p>'+$('#Income').val()+'</p>');
                $('#tdRace').append('<p >'+$('#Race').val()+'</p>');
                $('#tdWC').append('<p >'+$('#WaistCirc').val()+'</p>');
                $('#tdBMI').append('<p >'+$('#BMI').val()+'</p>');
                $('#tdA').append('<p >'+$('#Albuminuria').val()+'</p>');
                $('#tdUB').append('<p >'+$('#UrAlbCr').val()+'</p>');
                $('#tdUA').append('<p >'+$('#UricAcid').val()+'</p>');
                $('#tdBG').append('<p >'+$('#BloodGlucose').val()+'</p>');
                $('#tdHDL').append('<p >'+$('#HDL').val()+'</p>');
                $('#tdT').append('<p >'+$('#Triglycerides').val()+'</p>');
                if(response['pred']=='N')
                    $('#hfProb').append(`<b>Diagnostics</b>: Patient has <b style="color: #337ab7;">No Metabolic Syndrome</b> `)
                else if(response['pred']=='M')
                    $('#hfProb').append(`<b>Diagnostics</b>: Patient has <b style="color: #337ab7;">Metabolic Syndrome</b> `)



            }
        })
    });



});