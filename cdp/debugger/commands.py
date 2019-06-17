'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: debugger
Experimental: False
'''

from dataclasses import dataclass, field
import typing

from .types import *
from ..runtime import types as runtime



class Debugger:
    @staticmethod
    def continue_to_location(location: Location, target_call_frames: str) -> None:
        '''
        Continues execution until specific location is reached.
        
        :param location: Location to continue to.
        :param target_call_frames: 
        '''

        cmd_dict = {
            'method': 'Debugger.continueToLocation',
            'params': {
                'location': location,
                'targetCallFrames': target_call_frames,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def disable() -> None:
        '''
        Disables debugger for given page.
        '''

        cmd_dict = {
            'method': 'Debugger.disable',
        }
        response = yield cmd_dict

    @staticmethod
    def enable(max_scripts_cache_size: float) -> runtime.UniqueDebuggerId:
        '''
        Enables debugger for the given page. Clients should not assume that the debugging has been
        enabled until the result for this command is received.
        
        :param max_scripts_cache_size: The maximum size in bytes of collected scripts (not referenced by other heap objects)
        the debugger can hold. Puts no limit if paramter is omitted.
        :returns: Unique identifier of the debugger.
        '''

        cmd_dict = {
            'method': 'Debugger.enable',
            'params': {
                'maxScriptsCacheSize': max_scripts_cache_size,
            }
        }
        response = yield cmd_dict
        return runtime.UniqueDebuggerId.from_response(response['debuggerId'])

    @staticmethod
    def evaluate_on_call_frame(call_frame_id: CallFrameId, expression: str, object_group: str, include_command_line_api: bool, silent: bool, return_by_value: bool, generate_preview: bool, throw_on_side_effect: bool, timeout: runtime.TimeDelta) -> dict:
        '''
        Evaluates expression on a given call frame.
        
        :param call_frame_id: Call frame identifier to evaluate on.
        :param expression: Expression to evaluate.
        :param object_group: String object group name to put result into (allows rapid releasing resulting object handles
        using `releaseObjectGroup`).
        :param include_command_line_api: Specifies whether command line API should be available to the evaluated expression, defaults
        to false.
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause
        execution. Overrides `setPauseOnException` state.
        :param return_by_value: Whether the result is expected to be a JSON object that should be sent by value.
        :param generate_preview: Whether preview should be generated for the result.
        :param throw_on_side_effect: Whether to throw an exception if side effect cannot be ruled out during evaluation.
        :param timeout: Terminate execution after timing out (number of milliseconds).
        :returns: a dict with the following keys:
            * result: Object wrapper for the evaluation result.
            * exceptionDetails: Exception details.
        '''

        cmd_dict = {
            'method': 'Debugger.evaluateOnCallFrame',
            'params': {
                'callFrameId': call_frame_id,
                'expression': expression,
                'objectGroup': object_group,
                'includeCommandLineAPI': include_command_line_api,
                'silent': silent,
                'returnByValue': return_by_value,
                'generatePreview': generate_preview,
                'throwOnSideEffect': throw_on_side_effect,
                'timeout': timeout,
            }
        }
        response = yield cmd_dict
        return {
                'result': runtime.RemoteObject.from_response(response['result']),
                'exceptionDetails': runtime.ExceptionDetails.from_response(response['exceptionDetails']),
            }

    @staticmethod
    def get_possible_breakpoints(start: Location, end: Location, restrict_to_function: bool) -> typing.List['BreakLocation']:
        '''
        Returns possible locations for breakpoint. scriptId in start and end range locations should be
        the same.
        
        :param start: Start of range to search possible breakpoint locations in.
        :param end: End of range to search possible breakpoint locations in (excluding). When not specified, end
        of scripts is used as end of range.
        :param restrict_to_function: Only consider locations which are in the same (non-nested) function as start.
        :returns: List of the possible breakpoint locations.
        '''

        cmd_dict = {
            'method': 'Debugger.getPossibleBreakpoints',
            'params': {
                'start': start,
                'end': end,
                'restrictToFunction': restrict_to_function,
            }
        }
        response = yield cmd_dict
        return [BreakLocation.from_response(i) for i in response['locations']]

    @staticmethod
    def get_script_source(script_id: runtime.ScriptId) -> str:
        '''
        Returns source for the script with given id.
        
        :param script_id: Id of the script to get source for.
        :returns: Script source.
        '''

        cmd_dict = {
            'method': 'Debugger.getScriptSource',
            'params': {
                'scriptId': script_id,
            }
        }
        response = yield cmd_dict
        return str.from_response(response['scriptSource'])

    @staticmethod
    def get_stack_trace(stack_trace_id: runtime.StackTraceId) -> runtime.StackTrace:
        '''
        Returns stack trace with given `stackTraceId`.
        
        :param stack_trace_id: 
        :returns: 
        '''

        cmd_dict = {
            'method': 'Debugger.getStackTrace',
            'params': {
                'stackTraceId': stack_trace_id,
            }
        }
        response = yield cmd_dict
        return runtime.StackTrace.from_response(response['stackTrace'])

    @staticmethod
    def pause() -> None:
        '''
        Stops on the next JavaScript statement.
        '''

        cmd_dict = {
            'method': 'Debugger.pause',
        }
        response = yield cmd_dict

    @staticmethod
    def pause_on_async_call(parent_stack_trace_id: runtime.StackTraceId) -> None:
        '''
        
        
        :param parent_stack_trace_id: Debugger will pause when async call with given stack trace is started.
        '''

        cmd_dict = {
            'method': 'Debugger.pauseOnAsyncCall',
            'params': {
                'parentStackTraceId': parent_stack_trace_id,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def remove_breakpoint(breakpoint_id: BreakpointId) -> None:
        '''
        Removes JavaScript breakpoint.
        
        :param breakpoint_id: 
        '''

        cmd_dict = {
            'method': 'Debugger.removeBreakpoint',
            'params': {
                'breakpointId': breakpoint_id,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def restart_frame(call_frame_id: CallFrameId) -> dict:
        '''
        Restarts particular call frame from the beginning.
        
        :param call_frame_id: Call frame identifier to evaluate on.
        :returns: a dict with the following keys:
            * callFrames: New stack trace.
            * asyncStackTrace: Async stack trace, if any.
            * asyncStackTraceId: Async stack trace, if any.
        '''

        cmd_dict = {
            'method': 'Debugger.restartFrame',
            'params': {
                'callFrameId': call_frame_id,
            }
        }
        response = yield cmd_dict
        return {
                'callFrames': [CallFrame.from_response(i) for i in response['callFrames']],
                'asyncStackTrace': runtime.StackTrace.from_response(response['asyncStackTrace']),
                'asyncStackTraceId': runtime.StackTraceId.from_response(response['asyncStackTraceId']),
            }

    @staticmethod
    def resume() -> None:
        '''
        Resumes JavaScript execution.
        '''

        cmd_dict = {
            'method': 'Debugger.resume',
        }
        response = yield cmd_dict

    @staticmethod
    def search_in_content(script_id: runtime.ScriptId, query: str, case_sensitive: bool, is_regex: bool) -> typing.List['SearchMatch']:
        '''
        Searches for given string in script content.
        
        :param script_id: Id of the script to search in.
        :param query: String to search for.
        :param case_sensitive: If true, search is case sensitive.
        :param is_regex: If true, treats string parameter as regex.
        :returns: List of search matches.
        '''

        cmd_dict = {
            'method': 'Debugger.searchInContent',
            'params': {
                'scriptId': script_id,
                'query': query,
                'caseSensitive': case_sensitive,
                'isRegex': is_regex,
            }
        }
        response = yield cmd_dict
        return [SearchMatch.from_response(i) for i in response['result']]

    @staticmethod
    def set_async_call_stack_depth(max_depth: int) -> None:
        '''
        Enables or disables async call stacks tracking.
        
        :param max_depth: Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async
        call stacks (default).
        '''

        cmd_dict = {
            'method': 'Debugger.setAsyncCallStackDepth',
            'params': {
                'maxDepth': max_depth,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_blackbox_patterns(patterns: typing.List) -> None:
        '''
        Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in
        scripts with url matching one of the patterns. VM will try to leave blackboxed script by
        performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
        
        :param patterns: Array of regexps that will be used to check script url for blackbox state.
        '''

        cmd_dict = {
            'method': 'Debugger.setBlackboxPatterns',
            'params': {
                'patterns': patterns,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_blackboxed_ranges(script_id: runtime.ScriptId, positions: typing.List['ScriptPosition']) -> None:
        '''
        Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted
        scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
        Positions array contains positions where blackbox state is changed. First interval isn't
        blackboxed. Array should be sorted.
        
        :param script_id: Id of the script.
        :param positions: 
        '''

        cmd_dict = {
            'method': 'Debugger.setBlackboxedRanges',
            'params': {
                'scriptId': script_id,
                'positions': positions,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_breakpoint(location: Location, condition: str) -> dict:
        '''
        Sets JavaScript breakpoint at a given location.
        
        :param location: Location to set breakpoint in.
        :param condition: Expression to use as a breakpoint condition. When specified, debugger will only stop on the
        breakpoint if this expression evaluates to true.
        :returns: a dict with the following keys:
            * breakpointId: Id of the created breakpoint for further reference.
            * actualLocation: Location this breakpoint resolved into.
        '''

        cmd_dict = {
            'method': 'Debugger.setBreakpoint',
            'params': {
                'location': location,
                'condition': condition,
            }
        }
        response = yield cmd_dict
        return {
                'breakpointId': BreakpointId.from_response(response['breakpointId']),
                'actualLocation': Location.from_response(response['actualLocation']),
            }

    @staticmethod
    def set_instrumentation_breakpoint(instrumentation: str) -> BreakpointId:
        '''
        Sets instrumentation breakpoint.
        
        :param instrumentation: Instrumentation name.
        :returns: Id of the created breakpoint for further reference.
        '''

        cmd_dict = {
            'method': 'Debugger.setInstrumentationBreakpoint',
            'params': {
                'instrumentation': instrumentation,
            }
        }
        response = yield cmd_dict
        return BreakpointId.from_response(response['breakpointId'])

    @staticmethod
    def set_breakpoint_by_url(line_number: int, url: str, url_regex: str, script_hash: str, column_number: int, condition: str) -> dict:
        '''
        Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this
        command is issued, all existing parsed scripts will have breakpoints resolved and returned in
        `locations` property. Further matching script parsing will result in subsequent
        `breakpointResolved` events issued. This logical breakpoint will survive page reloads.
        
        :param line_number: Line number to set breakpoint at.
        :param url: URL of the resources to set breakpoint on.
        :param url_regex: Regex pattern for the URLs of the resources to set breakpoints on. Either `url` or
        `urlRegex` must be specified.
        :param script_hash: Script hash of the resources to set breakpoint on.
        :param column_number: Offset in the line to set breakpoint at.
        :param condition: Expression to use as a breakpoint condition. When specified, debugger will only stop on the
        breakpoint if this expression evaluates to true.
        :returns: a dict with the following keys:
            * breakpointId: Id of the created breakpoint for further reference.
            * locations: List of the locations this breakpoint resolved into upon addition.
        '''

        cmd_dict = {
            'method': 'Debugger.setBreakpointByUrl',
            'params': {
                'lineNumber': line_number,
                'url': url,
                'urlRegex': url_regex,
                'scriptHash': script_hash,
                'columnNumber': column_number,
                'condition': condition,
            }
        }
        response = yield cmd_dict
        return {
                'breakpointId': BreakpointId.from_response(response['breakpointId']),
                'locations': [Location.from_response(i) for i in response['locations']],
            }

    @staticmethod
    def set_breakpoint_on_function_call(object_id: runtime.RemoteObjectId, condition: str) -> BreakpointId:
        '''
        Sets JavaScript breakpoint before each call to the given function.
        If another function was created from the same source as a given one,
        calling it will also trigger the breakpoint.
        
        :param object_id: Function object id.
        :param condition: Expression to use as a breakpoint condition. When specified, debugger will
        stop on the breakpoint if this expression evaluates to true.
        :returns: Id of the created breakpoint for further reference.
        '''

        cmd_dict = {
            'method': 'Debugger.setBreakpointOnFunctionCall',
            'params': {
                'objectId': object_id,
                'condition': condition,
            }
        }
        response = yield cmd_dict
        return BreakpointId.from_response(response['breakpointId'])

    @staticmethod
    def set_breakpoints_active(active: bool) -> None:
        '''
        Activates / deactivates all breakpoints on the page.
        
        :param active: New value for breakpoints active state.
        '''

        cmd_dict = {
            'method': 'Debugger.setBreakpointsActive',
            'params': {
                'active': active,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_pause_on_exceptions(state: str) -> None:
        '''
        Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions or
        no exceptions. Initial pause on exceptions state is `none`.
        
        :param state: Pause on exceptions mode.
        '''

        cmd_dict = {
            'method': 'Debugger.setPauseOnExceptions',
            'params': {
                'state': state,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_return_value(new_value: runtime.CallArgument) -> None:
        '''
        Changes return value in top frame. Available only at return break position.
        
        :param new_value: New return value.
        '''

        cmd_dict = {
            'method': 'Debugger.setReturnValue',
            'params': {
                'newValue': new_value,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_script_source(script_id: runtime.ScriptId, script_source: str, dry_run: bool) -> dict:
        '''
        Edits JavaScript source live.
        
        :param script_id: Id of the script to edit.
        :param script_source: New content of the script.
        :param dry_run: If true the change will not actually be applied. Dry run may be used to get result
        description without actually modifying the code.
        :returns: a dict with the following keys:
            * callFrames: New stack trace in case editing has happened while VM was stopped.
            * stackChanged: Whether current call stack  was modified after applying the changes.
            * asyncStackTrace: Async stack trace, if any.
            * asyncStackTraceId: Async stack trace, if any.
            * exceptionDetails: Exception details if any.
        '''

        cmd_dict = {
            'method': 'Debugger.setScriptSource',
            'params': {
                'scriptId': script_id,
                'scriptSource': script_source,
                'dryRun': dry_run,
            }
        }
        response = yield cmd_dict
        return {
                'callFrames': [CallFrame.from_response(i) for i in response['callFrames']],
                'stackChanged': bool.from_response(response['stackChanged']),
                'asyncStackTrace': runtime.StackTrace.from_response(response['asyncStackTrace']),
                'asyncStackTraceId': runtime.StackTraceId.from_response(response['asyncStackTraceId']),
                'exceptionDetails': runtime.ExceptionDetails.from_response(response['exceptionDetails']),
            }

    @staticmethod
    def set_skip_all_pauses(skip: bool) -> None:
        '''
        Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc).
        
        :param skip: New value for skip pauses state.
        '''

        cmd_dict = {
            'method': 'Debugger.setSkipAllPauses',
            'params': {
                'skip': skip,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_variable_value(scope_number: int, variable_name: str, new_value: runtime.CallArgument, call_frame_id: CallFrameId) -> None:
        '''
        Changes value of variable in a callframe. Object-based scopes are not supported and must be
        mutated manually.
        
        :param scope_number: 0-based number of scope as was listed in scope chain. Only 'local', 'closure' and 'catch'
        scope types are allowed. Other scopes could be manipulated manually.
        :param variable_name: Variable name.
        :param new_value: New variable value.
        :param call_frame_id: Id of callframe that holds variable.
        '''

        cmd_dict = {
            'method': 'Debugger.setVariableValue',
            'params': {
                'scopeNumber': scope_number,
                'variableName': variable_name,
                'newValue': new_value,
                'callFrameId': call_frame_id,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def step_into(break_on_async_call: bool) -> None:
        '''
        Steps into the function call.
        
        :param break_on_async_call: Debugger will issue additional Debugger.paused notification if any async task is scheduled
        before next pause.
        '''

        cmd_dict = {
            'method': 'Debugger.stepInto',
            'params': {
                'breakOnAsyncCall': break_on_async_call,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def step_out() -> None:
        '''
        Steps out of the function call.
        '''

        cmd_dict = {
            'method': 'Debugger.stepOut',
        }
        response = yield cmd_dict

    @staticmethod
    def step_over() -> None:
        '''
        Steps over the statement.
        '''

        cmd_dict = {
            'method': 'Debugger.stepOver',
        }
        response = yield cmd_dict
